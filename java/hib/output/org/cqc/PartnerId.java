/*
*   $HeadURL:$
*   Created: 24-Apr-2012 11:57:32                       
*   Copyright (c) 2010, Matt Harrison. All rights reserved.
*/
package org.cqc;



/**
*   Data access object representing a PartnerId.
*
*   @author matth
*   @version $Rev: 2 $
*/
public class PartnerId  implements java.io.Serializable
{
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ FIELDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    private String providerId;
    
    private String partnerId;


    //~~~~~~~~~~~~~~~~~~~~~~~ CONSTRUCTORS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    /** Default constructor. */ 
    public PartnerId() 
    {
    }



    /** Full constructor. 
    *
    *   @param providerId
    *   @param partnerId
    */ 
    public PartnerId( String providerId, String partnerId ) 
    {
       this.providerId = providerId;
       this.partnerId = partnerId;
    }
   
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ METHODS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    /*  property: providerId  */
    /**
    *   Returns the value of property 'providerId'.   
    */
    public String getProviderId() 
    {
        return providerId;
    }
    
    /**
    *   Sets the value of property 'providerId'.    
    */
    public void setProviderId( String x ) 
    {
        providerId = x;
    }
    

    /*  property: partnerId  */
    /**
    *   Returns the value of property 'partnerId'.   
    */
    public String getPartnerId() 
    {
        return partnerId;
    }
    
    /**
    *   Sets the value of property 'partnerId'.    
    */
    public void setPartnerId( String x ) 
    {
        partnerId = x;
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
            + ": providerId=" 
            + providerId      
            + ", partnerId=" 
            + partnerId      
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
            
		if ( !(x instanceof PartnerId) ) 
		    return false;
		    
		PartnerId other = (PartnerId) x; 
		
		return this.providerId == other.providerId
		    && this.partnerId == other.partnerId;         
    }
   
   
    /**
    *   Overridden to generate a hashCode based on the current value of each of 
    *   this object's properties values.
    */
    @Override
    public int hashCode() 
    {
        int result = 17
            + providerId.hashCode()
            + partnerId.hashCode();  
            
        return result;
    }   

}


