/*
*   $HeadURL:$
*   Created: 24-Apr-2012 11:57:32                       
*   Copyright (c) 2010, Matt Harrison. All rights reserved.
*/
package org.cqc;



/**
*   Data access object representing a ChapterId.
*
*   @author matth
*   @version $Rev: 2 $
*/
public class ChapterId  implements java.io.Serializable
{
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ FIELDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    private String providerId;
    
    private String locationId;
    
    private String chapterId;


    //~~~~~~~~~~~~~~~~~~~~~~~ CONSTRUCTORS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    /** Default constructor. */ 
    public ChapterId() 
    {
    }



    /** Full constructor. 
    *
    *   @param providerId
    *   @param locationId
    *   @param chapterId
    */ 
    public ChapterId( String providerId, String locationId, String chapterId ) 
    {
       this.providerId = providerId;
       this.locationId = locationId;
       this.chapterId = chapterId;
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
    

    /*  property: chapterId  */
    /**
    *   Returns the value of property 'chapterId'.   
    */
    public String getChapterId() 
    {
        return chapterId;
    }
    
    /**
    *   Sets the value of property 'chapterId'.    
    */
    public void setChapterId( String x ) 
    {
        chapterId = x;
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
            + ", chapterId=" 
            + chapterId      
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
            
		if ( !(x instanceof ChapterId) ) 
		    return false;
		    
		ChapterId other = (ChapterId) x; 
		
		return this.providerId == other.providerId
		    && this.locationId == other.locationId
		    && this.chapterId == other.chapterId;         
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
            + chapterId.hashCode();  
            
        return result;
    }   

}


