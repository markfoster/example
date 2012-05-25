import java.util.*;
import java.text.*;
 import org.hibernate.EntityMode;
 import org.hibernate.Query;
 import org.hibernate.Session;
 import org.hibernate.Transaction;
 import org.dom4j.*;

 public class DynamicMapping {
    
     public static void main(String[] args) {
         Session session = HibernateUtil.getSessionFactory().openSession().getSession(EntityMode.DOM4J);

         Transaction tx = null;


	DateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
	String nowAsString = df.format(new Date());
        System.out.println("Now = " + nowAsString);

/**
         tx = session.beginTransaction();
 Query deleteQuery = session.createQuery("delete from Provider");
 deleteQuery.executeUpdate();
 tx.commit();
**/

 tx = session.beginTransaction();
         //create some some student and save them
         {
             Element e = null;
             Element entity = DocumentHelper.createElement("Provider");
             e = DocumentHelper.createElement("Provider_Id");
             e.setText("12345");
             entity.add(e);
             e = DocumentHelper.createElement("Name");
             e.setText("Alice111");
             entity.add(e);
             e = DocumentHelper.createElement("Last_Updated");
             e.setText(nowAsString);
             entity.add(e);
             session.save(entity);
         }
         tx.commit();

/**
         {
             Element anStudent = DocumentHelper.createElement("Student");
             Element nameElement = DocumentHelper.createElement("name");
             nameElement.setText("Lea");
            
             Element lastNameElement = DocumentHelper.createElement("lastName");
             lastNameElement.setText("Connor");
            
             anStudent.add(nameElement);
             anStudent.add(lastNameElement);
             session.save(anStudent);
         }
 **/       

/**
try {
Session pSession = HibernateUtil.getSessionFactory().openSession().getSession(EntityMode.POJO);
        //Session pSession = session.getSession(EntityMode.POJO);
        tx = pSession.beginTransaction();
        Provider p = new Provider();
        p.setProviderId("4715");
        p.setName("GENM");
        pSession.save(p);
        p = new Provider();
        p.setProviderId("4711");
        p.setName("GENM");
        pSession.save(p);
        p = new Provider();
        p.setProviderId("4712");
        p.setName("GENM");
        pSession.save(p);
        tx.commit();
        pSession.flush();
} catch (Exception ex) {
	System.out.println(ex);
}
**/

         //List all student
         Query q = session.createQuery("from Provider");
        
         List students = q.list();
         //org.dom4j.Element el = (org.dom4j.Element)students.get(0);
         //System.out.println(el.getText());
         for (Iterator it = students.iterator(); it.hasNext();) {
             org.dom4j.Element student = (org.dom4j.Element)it.next();
             System.out.println("Printing a Provider: ");
             for ( Iterator i = student.elementIterator(); i.hasNext(); ) {
                 Element element = (Element) i.next();
                 System.out.println( element.getName()+":  "+ element.getText());
             }
         }
         //retrieve an student, update and save it
 /**       
         q = session.createQuery("from Student where  name =:studentName ");
         q.setParameter("studentName", "Alice");
         Element alice = (Element) q.uniqueResult();
        
         alice.element("name").setText("No Alice any more");
         tx=session.beginTransaction();
         session.save(alice);
         tx.commit();
**/        
         session.close();
         HibernateUtil.shutdown();
     }
 }
