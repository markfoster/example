/*
*   $HeadURL:$
*   Created: 24-Apr-2012 11:57:32                       
*   Copyright (c) 2010, Matt Harrison. All rights reserved.
*/
package org.cqc;



/**
*   Data access object representing a NominatedIndividualId.
*
*   @author matth
*   @version $Rev: 2 $
*/
public class NominatedIndividualId  implements java.io.Serializable
{
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ FIELDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    private String providerId;
    
    private String locationId;
    
    private String regulatedActivityId;


    //~~~~~~~~~~~~~~~~~~~~~~~ CONSTRUCTORS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    /** Default constructor. */ 
    public NominatedIndividualId() 
    {
    }



    /** Full constructor. 
    *
    *   @param providerId
    *   @param locationId
    *   @param regulatedActivityId
    */ 
    public NominatedIndividualId( String providerId, String locationId, String regulatedActivityId ) 
    {
       this.providerId = providerId;
       this.locationId = locationId;
       this.regulatedActivityId = regulatedActivityId;
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
    

    /*  property: regulatedActivityId  */
    /**
    *   Returns the value of property 'regulatedActivityId'.   
    */
    public String getRegulatedActivityId() 
    {
        return regulatedActivityId;
    }
    
    /**
    *   Sets the value of property 'regulatedActivityId'.    
    */
    public void setRegulatedActivityId( String x ) 
    {
        regulatedActivityId = x;
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
            + ", regulatedActivityId=" 
            + regulatedActivityId      
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
            
		if ( !(x instanceof NominatedIndividualId) ) 
		    return false;
		    
		NominatedIndividualId other = (NominatedIndividualId) x; 
		
		return this.providerId == other.providerId
		    && this.locationId == other.locationId
		    && this.regulatedActivityId == other.regulatedActivityId;         
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
            + regulatedActivityId.hashCode();  
            
        return result;
    }   

}


