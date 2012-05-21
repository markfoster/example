/*
*   $HeadURL:$
*   Created: 24-Apr-2012 11:57:32                       
*   Copyright (c) 2010, Matt Harrison. All rights reserved.
*/
package org.cqc;



/**
*   Data access object representing a ComplianceCondition.
*
*   @author matth
*   @version $Rev: 2 $
*/
public class ComplianceCondition  implements java.io.Serializable
{
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ FIELDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    private ComplianceConditionId id;
    
    private String regulatedActivityId;
    
    private String complianceCondition;
    
    private String complianceReason;
    
    private String hashvalue;
    
    private Character action;


    //~~~~~~~~~~~~~~~~~~~~~~~ CONSTRUCTORS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    /** Default constructor. */ 
    public ComplianceCondition() 
    {
    }


    /** 
    *   Minimal constructor. 
    *
    *   @param id
    *   @param regulatedActivityId
    */ 
    public ComplianceCondition( ComplianceConditionId id, String regulatedActivityId ) 
    {
        this.id = id;
        this.regulatedActivityId = regulatedActivityId;
    }


    /** Full constructor. 
    *
    *   @param id
    *   @param regulatedActivityId
    *   @param complianceCondition
    *   @param complianceReason
    *   @param hashvalue
    *   @param action
    */ 
    public ComplianceCondition( ComplianceConditionId id, String regulatedActivityId, String complianceCondition, String complianceReason, String hashvalue, Character action ) 
    {
       this.id = id;
       this.regulatedActivityId = regulatedActivityId;
       this.complianceCondition = complianceCondition;
       this.complianceReason = complianceReason;
       this.hashvalue = hashvalue;
       this.action = action;
    }
   
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ METHODS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    /*  property: id  */
    /**
    *   Returns the value of property 'id'.   
    */
    public ComplianceConditionId getId() 
    {
        return id;
    }
    
    /**
    *   Sets the value of property 'id'.    
    */
    public void setId( ComplianceConditionId x ) 
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
    

    /*  property: complianceCondition  */
    /**
    *   Returns the value of property 'complianceCondition'.   
    */
    public String getComplianceCondition() 
    {
        return complianceCondition;
    }
    
    /**
    *   Sets the value of property 'complianceCondition'.    
    */
    public void setComplianceCondition( String x ) 
    {
        complianceCondition = x;
    }
    

    /*  property: complianceReason  */
    /**
    *   Returns the value of property 'complianceReason'.   
    */
    public String getComplianceReason() 
    {
        return complianceReason;
    }
    
    /**
    *   Sets the value of property 'complianceReason'.    
    */
    public void setComplianceReason( String x ) 
    {
        complianceReason = x;
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
            + ", complianceCondition=" 
            + complianceCondition      
            + ", complianceReason=" 
            + complianceReason      
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
            
		if ( !(x instanceof ComplianceCondition) ) 
		    return false;
		    
		ComplianceCondition other = (ComplianceCondition) x; 
		
		return this.id == other.id
		    && this.regulatedActivityId == other.regulatedActivityId
		    && this.complianceCondition == other.complianceCondition
		    && this.complianceReason == other.complianceReason
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
            + complianceCondition.hashCode()
            + complianceReason.hashCode()
            + hashvalue.hashCode()
            + action.hashCode();  
            
        return result;
    }   

}


