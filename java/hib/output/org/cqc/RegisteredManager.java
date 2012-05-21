/*
*   $HeadURL:$
*   Created: 24-Apr-2012 11:57:32                       
*   Copyright (c) 2010, Matt Harrison. All rights reserved.
*/
package org.cqc;



/**
*   Data access object representing a RegisteredManager.
*
*   @author matth
*   @version $Rev: 2 $
*/
public class RegisteredManager  implements java.io.Serializable
{
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ FIELDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    private RegisteredManagerId id;
    
    private String managerName;
    
    private String managerCondition;
    
    private String hashvalue;
    
    private Character action;


    //~~~~~~~~~~~~~~~~~~~~~~~ CONSTRUCTORS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    /** Default constructor. */ 
    public RegisteredManager() 
    {
    }


    /** 
    *   Minimal constructor. 
    *
    *   @param id
    */ 
    public RegisteredManager( RegisteredManagerId id ) 
    {
        this.id = id;
    }


    /** Full constructor. 
    *
    *   @param id
    *   @param managerName
    *   @param managerCondition
    *   @param hashvalue
    *   @param action
    */ 
    public RegisteredManager( RegisteredManagerId id, String managerName, String managerCondition, String hashvalue, Character action ) 
    {
       this.id = id;
       this.managerName = managerName;
       this.managerCondition = managerCondition;
       this.hashvalue = hashvalue;
       this.action = action;
    }
   
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ METHODS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    /*  property: id  */
    /**
    *   Returns the value of property 'id'.   
    */
    public RegisteredManagerId getId() 
    {
        return id;
    }
    
    /**
    *   Sets the value of property 'id'.    
    */
    public void setId( RegisteredManagerId x ) 
    {
        id = x;
    }
    

    /*  property: managerName  */
    /**
    *   Returns the value of property 'managerName'.   
    */
    public String getManagerName() 
    {
        return managerName;
    }
    
    /**
    *   Sets the value of property 'managerName'.    
    */
    public void setManagerName( String x ) 
    {
        managerName = x;
    }
    

    /*  property: managerCondition  */
    /**
    *   Returns the value of property 'managerCondition'.   
    */
    public String getManagerCondition() 
    {
        return managerCondition;
    }
    
    /**
    *   Sets the value of property 'managerCondition'.    
    */
    public void setManagerCondition( String x ) 
    {
        managerCondition = x;
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
            + ", managerName=" 
            + managerName      
            + ", managerCondition=" 
            + managerCondition      
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
            
		if ( !(x instanceof RegisteredManager) ) 
		    return false;
		    
		RegisteredManager other = (RegisteredManager) x; 
		
		return this.id == other.id
		    && this.managerName == other.managerName
		    && this.managerCondition == other.managerCondition
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
            + managerName.hashCode()
            + managerCondition.hashCode()
            + hashvalue.hashCode()
            + action.hashCode();  
            
        return result;
    }   

}


