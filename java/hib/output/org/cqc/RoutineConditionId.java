/*
*   $HeadURL:$
*   Created: 24-Apr-2012 11:57:32                       
*   Copyright (c) 2010, Matt Harrison. All rights reserved.
*/
package org.cqc;



/**
*   Data access object representing a RoutineConditionId.
*
*   @author matth
*   @version $Rev: 2 $
*/
public class RoutineConditionId  implements java.io.Serializable
{
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ FIELDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    private String providerId;
    
    private String locationId;
    
    private String conditionId;


    //~~~~~~~~~~~~~~~~~~~~~~~ CONSTRUCTORS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    /** Default constructor. */ 
    public RoutineConditionId() 
    {
    }



    /** Full constructor. 
    *
    *   @param providerId
    *   @param locationId
    *   @param conditionId
    */ 
    public RoutineConditionId( String providerId, String locationId, String conditionId ) 
    {
       this.providerId = providerId;
       this.locationId = locationId;
       this.conditionId = conditionId;
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
    

    /*  property: conditionId  */
    /**
    *   Returns the value of property 'conditionId'.   
    */
    public String getConditionId() 
    {
        return conditionId;
    }
    
    /**
    *   Sets the value of property 'conditionId'.    
    */
    public void setConditionId( String x ) 
    {
        conditionId = x;
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
            + ", conditionId=" 
            + conditionId      
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
            
		if ( !(x instanceof RoutineConditionId) ) 
		    return false;
		    
		RoutineConditionId other = (RoutineConditionId) x; 
		
		return this.providerId == other.providerId
		    && this.locationId == other.locationId
		    && this.conditionId == other.conditionId;         
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
            + conditionId.hashCode();  
            
        return result;
    }   

}


