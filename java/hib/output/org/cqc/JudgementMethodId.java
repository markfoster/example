/*
*   $HeadURL:$
*   Created: 24-Apr-2012 11:57:32                       
*   Copyright (c) 2010, Matt Harrison. All rights reserved.
*/
package org.cqc;



/**
*   Data access object representing a JudgementMethodId.
*
*   @author matth
*   @version $Rev: 2 $
*/
public class JudgementMethodId  implements java.io.Serializable
{
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ FIELDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    private String providerId;
    
    private String locationId;
    
    private String outcomeId;
    
    private String methodId;


    //~~~~~~~~~~~~~~~~~~~~~~~ CONSTRUCTORS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    /** Default constructor. */ 
    public JudgementMethodId() 
    {
    }



    /** Full constructor. 
    *
    *   @param providerId
    *   @param locationId
    *   @param outcomeId
    *   @param methodId
    */ 
    public JudgementMethodId( String providerId, String locationId, String outcomeId, String methodId ) 
    {
       this.providerId = providerId;
       this.locationId = locationId;
       this.outcomeId = outcomeId;
       this.methodId = methodId;
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
    

    /*  property: locationId  */
    /**
    *   Returns the value of property 'locationId'.   
    */
    public String getLocationId() 
    {
        return locationId;
    }
    
    /**
    *   Sets the value of property 'locationId'.    
    */
    public void setLocationId( String x ) 
    {
        locationId = x;
    }
    

    /*  property: outcomeId  */
    /**
    *   Returns the value of property 'outcomeId'.   
    */
    public String getOutcomeId() 
    {
        return outcomeId;
    }
    
    /**
    *   Sets the value of property 'outcomeId'.    
    */
    public void setOutcomeId( String x ) 
    {
        outcomeId = x;
    }
    

    /*  property: methodId  */
    /**
    *   Returns the value of property 'methodId'.   
    */
    public String getMethodId() 
    {
        return methodId;
    }
    
    /**
    *   Sets the value of property 'methodId'.    
    */
    public void setMethodId( String x ) 
    {
        methodId = x;
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
            + ", locationId=" 
            + locationId      
            + ", outcomeId=" 
            + outcomeId      
            + ", methodId=" 
            + methodId      
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
            
		if ( !(x instanceof JudgementMethodId) ) 
		    return false;
		    
		JudgementMethodId other = (JudgementMethodId) x; 
		
		return this.providerId == other.providerId
		    && this.locationId == other.locationId
		    && this.outcomeId == other.outcomeId
		    && this.methodId == other.methodId;         
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
            + locationId.hashCode()
            + outcomeId.hashCode()
            + methodId.hashCode();  
            
        return result;
    }   

}


