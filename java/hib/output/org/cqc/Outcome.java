/*
*   $HeadURL:$
*   Created: 24-Apr-2012 11:57:32                       
*   Copyright (c) 2010, Matt Harrison. All rights reserved.
*/
package org.cqc;



/**
*   Data access object representing a Outcome.
*
*   @author matth
*   @version $Rev: 2 $
*/
public class Outcome  implements java.io.Serializable
{
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ FIELDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    private OutcomeId id;
    
    private String judgementId;
    
    private String judgementDate;
    
    private String judgementReason;
    
    private String judgementUserExperience;
    
    private String judgementOtherEvidence;
    
    private String judgementScoreId;
    
    private String outcomeStatementId;
    
    private String judgementSummary;
    
    private String hashvalue;
    
    private Character action;


    //~~~~~~~~~~~~~~~~~~~~~~~ CONSTRUCTORS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    /** Default constructor. */ 
    public Outcome() 
    {
    }


    /** 
    *   Minimal constructor. 
    *
    *   @param id
    */ 
    public Outcome( OutcomeId id ) 
    {
        this.id = id;
    }


    /** Full constructor. 
    *
    *   @param id
    *   @param judgementId
    *   @param judgementDate
    *   @param judgementReason
    *   @param judgementUserExperience
    *   @param judgementOtherEvidence
    *   @param judgementScoreId
    *   @param outcomeStatementId
    *   @param judgementSummary
    *   @param hashvalue
    *   @param action
    */ 
    public Outcome( OutcomeId id, String judgementId, String judgementDate, String judgementReason, String judgementUserExperience, String judgementOtherEvidence, String judgementScoreId, String outcomeStatementId, String judgementSummary, String hashvalue, Character action ) 
    {
       this.id = id;
       this.judgementId = judgementId;
       this.judgementDate = judgementDate;
       this.judgementReason = judgementReason;
       this.judgementUserExperience = judgementUserExperience;
       this.judgementOtherEvidence = judgementOtherEvidence;
       this.judgementScoreId = judgementScoreId;
       this.outcomeStatementId = outcomeStatementId;
       this.judgementSummary = judgementSummary;
       this.hashvalue = hashvalue;
       this.action = action;
    }
   
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ METHODS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    /*  property: id  */
    /**
    *   Returns the value of property 'id'.   
    */
    public OutcomeId getId() 
    {
        return id;
    }
    
    /**
    *   Sets the value of property 'id'.    
    */
    public void setId( OutcomeId x ) 
    {
        id = x;
    }
    

    /*  property: judgementId  */
    /**
    *   Returns the value of property 'judgementId'.   
    */
    public String getJudgementId() 
    {
        return judgementId;
    }
    
    /**
    *   Sets the value of property 'judgementId'.    
    */
    public void setJudgementId( String x ) 
    {
        judgementId = x;
    }
    

    /*  property: judgementDate  */
    /**
    *   Returns the value of property 'judgementDate'.   
    */
    public String getJudgementDate() 
    {
        return judgementDate;
    }
    
    /**
    *   Sets the value of property 'judgementDate'.    
    */
    public void setJudgementDate( String x ) 
    {
        judgementDate = x;
    }
    

    /*  property: judgementReason  */
    /**
    *   Returns the value of property 'judgementReason'.   
    */
    public String getJudgementReason() 
    {
        return judgementReason;
    }
    
    /**
    *   Sets the value of property 'judgementReason'.    
    */
    public void setJudgementReason( String x ) 
    {
        judgementReason = x;
    }
    

    /*  property: judgementUserExperience  */
    /**
    *   Returns the value of property 'judgementUserExperience'.   
    */
    public String getJudgementUserExperience() 
    {
        return judgementUserExperience;
    }
    
    /**
    *   Sets the value of property 'judgementUserExperience'.    
    */
    public void setJudgementUserExperience( String x ) 
    {
        judgementUserExperience = x;
    }
    

    /*  property: judgementOtherEvidence  */
    /**
    *   Returns the value of property 'judgementOtherEvidence'.   
    */
    public String getJudgementOtherEvidence() 
    {
        return judgementOtherEvidence;
    }
    
    /**
    *   Sets the value of property 'judgementOtherEvidence'.    
    */
    public void setJudgementOtherEvidence( String x ) 
    {
        judgementOtherEvidence = x;
    }
    

    /*  property: judgementScoreId  */
    /**
    *   Returns the value of property 'judgementScoreId'.   
    */
    public String getJudgementScoreId() 
    {
        return judgementScoreId;
    }
    
    /**
    *   Sets the value of property 'judgementScoreId'.    
    */
    public void setJudgementScoreId( String x ) 
    {
        judgementScoreId = x;
    }
    

    /*  property: outcomeStatementId  */
    /**
    *   Returns the value of property 'outcomeStatementId'.   
    */
    public String getOutcomeStatementId() 
    {
        return outcomeStatementId;
    }
    
    /**
    *   Sets the value of property 'outcomeStatementId'.    
    */
    public void setOutcomeStatementId( String x ) 
    {
        outcomeStatementId = x;
    }
    

    /*  property: judgementSummary  */
    /**
    *   Returns the value of property 'judgementSummary'.   
    */
    public String getJudgementSummary() 
    {
        return judgementSummary;
    }
    
    /**
    *   Sets the value of property 'judgementSummary'.    
    */
    public void setJudgementSummary( String x ) 
    {
        judgementSummary = x;
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
            + ", judgementId=" 
            + judgementId      
            + ", judgementDate=" 
            + judgementDate      
            + ", judgementReason=" 
            + judgementReason      
            + ", judgementUserExperience=" 
            + judgementUserExperience      
            + ", judgementOtherEvidence=" 
            + judgementOtherEvidence      
            + ", judgementScoreId=" 
            + judgementScoreId      
            + ", outcomeStatementId=" 
            + outcomeStatementId      
            + ", judgementSummary=" 
            + judgementSummary      
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
            
		if ( !(x instanceof Outcome) ) 
		    return false;
		    
		Outcome other = (Outcome) x; 
		
		return this.id == other.id
		    && this.judgementId == other.judgementId
		    && this.judgementDate == other.judgementDate
		    && this.judgementReason == other.judgementReason
		    && this.judgementUserExperience == other.judgementUserExperience
		    && this.judgementOtherEvidence == other.judgementOtherEvidence
		    && this.judgementScoreId == other.judgementScoreId
		    && this.outcomeStatementId == other.outcomeStatementId
		    && this.judgementSummary == other.judgementSummary
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
            + judgementId.hashCode()
            + judgementDate.hashCode()
            + judgementReason.hashCode()
            + judgementUserExperience.hashCode()
            + judgementOtherEvidence.hashCode()
            + judgementScoreId.hashCode()
            + outcomeStatementId.hashCode()
            + judgementSummary.hashCode()
            + hashvalue.hashCode()
            + action.hashCode();  
            
        return result;
    }   

}


