/*
*   $HeadURL:$
*   Created: 24-Apr-2012 11:57:32                       
*   Copyright (c) 2010, Matt Harrison. All rights reserved.
*/
package org.cqc;



/**
*   Data access object representing a RoutineCondition.
*
*   @author matth
*   @version $Rev: 2 $
*/
public class RoutineCondition  implements java.io.Serializable
{
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ FIELDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    private RoutineConditionId id;
    
    private String regulatedActivityId;
    
    private String routineCondition;
    
    private String hashvalue;
    
    private Character action;


    //~~~~~~~~~~~~~~~~~~~~~~~ CONSTRUCTORS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    /** Default constructor. */ 
    public RoutineCondition() 
    {
    }


    /** 
    *   Minimal constructor. 
    *
    *   @param id
    *   @param regulatedActivityId
    */ 
    public RoutineCondition( RoutineConditionId id, String regulatedActivityId ) 
    {
        this.id = id;
        this.regulatedActivityId = regulatedActivityId;
    }


    /** Full constructor. 
    *
    *   @param id
    *   @param regulatedActivityId
    *   @param routineCondition
    *   @param hashvalue
    *   @param action
    */ 
    public RoutineCondition( RoutineConditionId id, String regulatedActivityId, String routineCondition, String hashvalue, Character action ) 
    {
       this.id = id;
       this.regulatedActivityId = regulatedActivityId;
       this.routineCondition = routineCondition;
       this.hashvalue = hashvalue;
       this.action = action;
    }
   
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ METHODS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    /*  property: id  */
    /**
    *   Returns the value of property 'id'.   
    */
    public RoutineConditionId getId() 
    {
        return id;
    }
    
    /**
    *   Sets the value of property 'id'.    
    */
    public void setId( RoutineConditionId x ) 
    {
        id = x;
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
    

    /*  property: routineCondition  */
    /**
    *   Returns the value of property 'routineCondition'.   
    */
    public String getRoutineCondition() 
    {
        return routineCondition;
    }
    
    /**
    *   Sets the value of property 'routineCondition'.    
    */
    public void setRoutineCondition( String x ) 
    {
        routineCondition = x;
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
            + ", regulatedActivityId=" 
            + regulatedActivityId      
            + ", routineCondition=" 
            + routineCondition      
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
            
		if ( !(x instanceof RoutineCondition) ) 
		    return false;
		    
		RoutineCondition other = (RoutineCondition) x; 
		
		return this.id == other.id
		    && this.regulatedActivityId == other.regulatedActivityId
		    && this.routineCondition == other.routineCondition
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
            + regulatedActivityId.hashCode()
            + routineCondition.hashCode()
            + hashvalue.hashCode()
            + action.hashCode();  
            
        return result;
    }   

}

