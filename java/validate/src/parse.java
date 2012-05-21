
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.XMLConstants;
import javax.xml.transform.stream.StreamSource;
import javax.xml.validation.SchemaFactory;
import javax.xml.validation.Schema;
import javax.xml.validation.Validator;

import org.xml.sax.ErrorHandler;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;
import org.w3c.dom.Document;
import org.w3c.dom.*;
import org.w3c.dom.NodeList;
import org.apache.log4j.Logger;
import org.xml.sax.InputSource;

import java.io.*;
import java.io.StringReader;
import java.util.*;

import org.dom4j.DocumentHelper;
import org.dom4j.Element;
import org.dom4j.io.SAXReader;
import org.dom4j.io.XMLWriter;
import org.dom4j.io.OutputFormat;

import org.hibernate.EntityMode;
import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.Transaction;

public class parse {

	//Logger logger = Logger.getLogger(this.getClass().getName());
	Logger logger = Logger.getLogger("stdout");

        public static void main(String[] arg) throws IOException {

                HibernateUtil.buildSessionFactory();

                System.out.println("Hello");
                parse p = new parse();

                String xml = fileToString("hbm/Geocode.hbm.xml");
                if (p.checkXML(xml) != null) System.out.println("XML is well formed");

                xml = fileToString("xml/audit.xml");
                String xsd = fileToString("xsd/audit.xsd");
		String result = "";
                if (p.checkXML(xml) != null) System.out.println("XML is well formed");
                result = p.checkXSD(xsd);
                System.out.println(result);
 		result = p.validateXML(xml, xsd);
                System.out.println(result);

                Map<String, Document> docs = new HashMap();

		// Parse the audit file
		Map audits = p.parse(xml);
                Set keys = audits.keySet();
                Iterator i = keys.iterator();
                while (i.hasNext()) {
                       String key = (String)i.next();
		       String xmlFile = "xml/" + key + ".xml";
		       String xsdFile = "xsd/" + key + ".xsd";
		       System.out.println("Looking to load " + xmlFile);
	               xml = fileToString(xmlFile);	
	               xsd = fileToString(xsdFile);	
                       Document doc = p.checkXML(xml);
                       docs.put(key, doc);
                       p.validateXML(xml, xsd);
                       //System.out.print(key + ": ");
                       //System.out.println(smap.get(key));
                }

		int updates = Integer.parseInt("1");
                System.out.println("Updates = " + updates);

		//p.saveProviders();
		//p.saveOutcomes();
                //p.readGeocodes();
        }

        public void readGeocodes() {
                Session session = null;
                try {
                        //session = HibernateUtil.getSessionFactory().openSession().getSession(EntityMode.DOM4J);
                        session = HibernateUtil.currentSession();
                        // List all providers
                        Session dom4jSession = session.getSession(EntityMode.DOM4J);
                        Query q = dom4jSession.createQuery("FROM cqc_address_cache");
                        List results = q.list();
                        org.dom4j.Document document = DocumentHelper.createDocument();
                        Element rootElement = document.addElement("Geocodes");
                        for (int i = 0; i < results.size(); i++) {
                                Element catalog = (Element) results.get(i);
                                rootElement.add(catalog);
                        }
                        OutputFormat format = OutputFormat.createPrettyPrint();
                } catch(Exception e) {
                        e.printStackTrace();
                        System.out.println(e.getMessage());
                } finally {
                        session.close();
                }
        }

	public void saveProviders() {
		Session session = null;
		try {
			//session = HibernateUtil.getSessionFactory().openSession().getSession(EntityMode.DOM4J);
			session = HibernateUtil.currentSession();
	        	// List all providers
			Session dom4jSession = session.getSession(EntityMode.DOM4J);
			Query q = dom4jSession.createQuery("FROM Provider");
			List results = q.list();
            		org.dom4j.Document document = DocumentHelper.createDocument();
            		Element rootElement = document.addElement("Providers");
            		for (int i = 0; i < results.size(); i++) {
                		Element catalog = (Element) results.get(i);
                		rootElement.add(catalog);
            		}
            		OutputFormat format = OutputFormat.createPrettyPrint();

            		XMLWriter output = new XMLWriter(new FileWriter(new java.io.File("/tmp/providers.xml")), format);
            		output.setIndentLevel(1);
            		output.write(document);
            		output.close();

            		StringWriter sw = new StringWriter();
            		XMLWriter writer = new XMLWriter(sw, format);
            		writer.write(document);
            		System.out.println(sw.toString());
		} catch(Exception e) {
			e.printStackTrace();
			System.out.println(e.getMessage());
		} finally {
			session.close();
		}
	}
 
        public Map parse(String xml) {
 		Document doc = null;
		try {
			DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
			DocumentBuilder builder = factory.newDocumentBuilder();
			doc = builder.parse(new InputSource(new StringReader(xml)));
                } catch (Exception e) {
                        logger.error("Error", e);
                        return null;
                }
		TreeMap<String, Map<String, String>> smap = new TreeMap<String, Map<String, String>>();
 		visit(smap, doc, 0);
/**
                Set keys = smap.keySet(); 
                Iterator i = keys.iterator();
                while (i.hasNext()) {
                       String key = (String)i.next();  
		       System.out.print(key + ": "); 
		       System.out.println(smap.get(key));
                }
**/
 		return smap; 
	}

 	public void visit(Map map, Node n, int level) {
                NodeList nl = n.getChildNodes();
                for(int i=0,count=nl.getLength(); i<count; i++) {
                    if (nl.item(i).getNodeType() == Node.ELEMENT_NODE) {
			if (nl.item(i).hasAttributes()) {
                	    getAttributes(map, nl.item(i));
            		}
                        visit(map, nl.item(i), level+1);
                    }
                }
	}

    	private void getAttributes(Map map, Node node) {
        	NamedNodeMap attrs = node.getAttributes();
        	//System.out.print(node.getNodeName());
                Map<String, String> attrMap = new HashMap<String, String>();
        	for (int i = 0; i < attrs.getLength(); i++) {
                     Attr attribute = (Attr)attrs.item(i);
            	     //System.out.print(" : " + attribute.getName() + "=" + attribute.getValue());
                     attrMap.put((String)attribute.getName(), (String)attribute.getValue());
        	}
                map.put(node.getNodeName(), attrMap);
    	}

	public Document checkXML(String xml) {
		logger.info("in checkXML()");
                Document doc = null;
		try {
			DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
			DocumentBuilder builder = factory.newDocumentBuilder();
			doc = builder.parse(new InputSource(new StringReader(xml)));
		} catch (Exception e) {
			logger.error("Error", e);
			return null;
		}
		logger.info("The XML is Well Formed");
                return doc;
	}

	public String checkXSD(String xsd) {
		logger.info("in checkXSD()");
		try {
			SchemaFactory factory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
			factory.newSchema(new StreamSource(new StringReader(xsd)));
		} catch (Exception e) {
			logger.error("Error", e);
			return e.getMessage();
		}
		return "The XSD is Valid";
	}

        public String validateXML(String xml, String xsd) {
 		logger.info("in validateXML()");
		MyErrorHandler errorHandler = new MyErrorHandler();
		try {
			SchemaFactory factory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
			Schema schema = factory.newSchema(new StreamSource(new StringReader(xsd)));
			Validator validator = schema.newValidator();
			validator.setErrorHandler(errorHandler);
			validator.validate(new StreamSource(new StringReader(xml)));
		} catch (Exception e) {
			logger.error("Error", e);
			return e.getMessage();
		}

		String getResult = errorHandler.getResult();
		if (getResult.isEmpty())
			return "The XML is Well Formed and VALID";
		return getResult;
        }

	static class MyErrorHandler implements ErrorHandler {
		StringBuilder result = new StringBuilder();
		public void fatalError(SAXParseException e) throws SAXException {
			result.append(e.toString());
		}
		public void error(SAXParseException e) throws SAXException {
			result.append(e.toString());
		}
		public void warning(SAXParseException e) throws SAXException {
			result.append(e.toString());
		}
		public String getResult() {
			return result.toString();
		}
	}

    /**
     * Description of the Method
     *
     * @param file
     *          The file to be turned into a String
     * @return  The file as String encoded in the platform
     * default encoding
     */
private static String fileToString( String file ) throws IOException {
    BufferedReader reader = new BufferedReader( new FileReader (file));
    String line  = null;
    StringBuilder stringBuilder = new StringBuilder();
    String ls = System.getProperty("line.separator");
    while( ( line = reader.readLine() ) != null ) {
        stringBuilder.append( line );
        stringBuilder.append( ls );
    }
    return stringBuilder.toString();
 }

}
