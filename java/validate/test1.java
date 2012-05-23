import java.io.*;
import java.net.MalformedURLException;
import java.net.URL;
import org.xml.sax.SAXException;
 
 
/**
 * A simple demo of Xalan 1. This code was originally written using
 * Xalan 1.2.2.  It will not work with Xalan 2.
 */
public class test1 {
 
    /**
     * Accept two command line arguments: the name of an XML file, and
     * the name of an XSLT stylesheet. The result of the transformation
     * is written to stdout.
     */
    public static void main(String[] args)
            throws MalformedURLException, SAXException {
        if (args.length != 2) {
            System.err.println("Usage:");
            System.err.println("  java " + test1.class.getName(  )
                    + " xmlFileName xsltFileName");
            System.exit(1);
        }
 
        String xmlFileName = args[0];
        String xsltFileName = args[1];
 
        String xmlSystemId = new File(xmlFileName).toURL().toExternalForm(  );
        String xsltSystemId = new File(xsltFileName).toURL().toExternalForm(  );
 
        org.apache.xalan.xslt.XSLTProcessor processor =
                org.apache.xalan.xslt.XSLTProcessorFactory.getProcessor(  );
 
        org.apache.xalan.xslt.XSLTInputSource xmlInputSource =
                new org.apache.xalan.xslt.XSLTInputSource(xmlSystemId);
 
        org.apache.xalan.xslt.XSLTInputSource xsltInputSource =
                new org.apache.xalan.xslt.XSLTInputSource(xsltSystemId);
 
        org.apache.xalan.xslt.XSLTResultTarget resultTree =
                new org.apache.xalan.xslt.XSLTResultTarget(System.out);
 
        processor.process(xmlInputSource, xsltInputSource, resultTree);
    }
}
