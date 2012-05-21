/*
*   $HeadURL:$
*   Created: 24-Apr-2012 11:57:32                       
*   Copyright (c) 2010, Matt Harrison. All rights reserved.
*/
package org.cqc;



/**
*   Data access object representing a JudgementMethod.
*
*   @author matth
*   @version $Rev: 2 $
*/
public class JudgementMethod  implements java.io.Serializable
{
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ FIELDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    private JudgementMethodId id;
    
    private String methodText;
    
    private String hashvalue;
    
    private Character action;


    //~~~~~~~~~~~~~~~~~~~~~~~ CONSTRUCTORS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    /** Default constructor. */ 
    public JudgementMethod() 
    {
    }


    /** 
    *   Minimal constructor. 
    *
    *   @param id
    */ 
    public JudgementMethod( JudgementMethodId id ) 
    {
        this.id = id;
    }


    /** Full constructor. 
    *
    *   @param id
    *   @param methodText
    *   @param hashvalue
    *   @param action
    */ 
    public JudgementMethod( JudgementMethodId id, String methodText, String hashvalue, Character action ) 
    {
       this.id = id;
       this.methodText = methodText;
       this.hashvalue = hashvalue;
       this.action = action;
    }
   
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ METHODS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    /*  property: id  */
    /**
    *   Returns the value of property 'id'.   
    */
    public JudgementMethodId getId() 
    {
        return id;
    }
    
    /**
    *   Sets the value of property 'id'.    
    */
    public void setId( JudgementMethodId x ) 
    {
        id = x;
    }
    

    /*  property: methodText  */
    /**
    *   Returns the value of property 'methodText'.   
    */
    public String getMethodText() 
    {
        return methodText;
    }
    
    /**
    *   Sets the value of property 'methodText'.    
    */
    public void setMethodText( String x ) 
    {
        methodText = x;
    }
    

    /*  property: hashvalue  */
    /**
    *   Returns the value of property 'hashvalue'.   
    */
    public String getHashvalue() 
    {
        return hashvalue;
    }
    
    /**
    *   Sets the value of property 'hashvalue'.    
    */
    public void setHashvalue( String x ) 
    {
        hashvalue = x;
    }
    

    /*  property: action  */
    /**
    *   Returns the value of property 'action'.   
    */
    public Character getAction() 
    {
        return action;
    }
    
    /**
    *   Sets the value of property 'action'.    
    */
    public void setAction( Character x ) 
    {
        action = x;
    }
    



    /*  overridden from Object  */

    /**
    *   Returns a String version of this DAO, including the runtime {@link Class} 
    *   name, hashCode, and current property values.
    */
    @Override
    public String toString() 
    {
        return "["
            + getClass().getSimpleName()      
            + ": id=" 
            + id      
            + ", methodText=" 
            + methodText      
            + ", hashvalue=" 
            + hashvalue      
            + ", action=" 
            + action      
            + "]"
        ;			
    }

    
    /**
    *   Returns whether the given {@link Object} is equal to this
    *   Object by <em>value</em>; that is, it compares the value of 
    *   every property of each of the objects.
    *   
    *   @see #hashCode()
    */
    @Override
    public boolean equals( Object x ) 
    {
        if ( this == x ) 
            return true;
		 
        if ( x == null ) 
            return false;
            
		if ( !(x instanceof JudgementMethod) ) 
		    return false;
		    
		JudgementMethod other = (JudgementMethod) x; 
		
		return this.id == other.id
		    && this.methodText == other.methodText
		    && this.hashvalue == other.hashvalue
		    && this.action == other.action;         
    }
   
   
    /**
    *   Overridden to generate a hashCode based on the current value of each of 
    *   this object's properties values.
    */
    @Override
    public int hashCode() 
    {
        int result = 17
            + id.hashCode()
            + methodText.hashCode()
            + hashvalue.hashCode()
            + action.hashCode();  
            
        return result;
    }   

}


