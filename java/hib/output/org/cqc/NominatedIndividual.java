/*
*   $HeadURL:$
*   Created: 24-Apr-2012 11:57:32                       
*   Copyright (c) 2010, Matt Harrison. All rights reserved.
*/
package org.cqc;



/**
*   Data access object representing a NominatedIndividual.
*
*   @author matth
*   @version $Rev: 2 $
*/
public class NominatedIndividual  implements java.io.Serializable
{
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ FIELDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    private NominatedIndividualId id;
    
    private String nominatedIndividual;
    
    private String hashvalue;
    
    private Character action;


    //~~~~~~~~~~~~~~~~~~~~~~~ CONSTRUCTORS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    /** Default constructor. */ 
    public NominatedIndividual() 
    {
    }


    /** 
    *   Minimal constructor. 
    *
    *   @param id
    */ 
    public NominatedIndividual( NominatedIndividualId id ) 
    {
        this.id = id;
    }


    /** Full constructor. 
    *
    *   @param id
    *   @param nominatedIndividual
    *   @param hashvalue
    *   @param action
    */ 
    public NominatedIndividual( NominatedIndividualId id, String nominatedIndividual, String hashvalue, Character action ) 
    {
       this.id = id;
       this.nominatedIndividual = nominatedIndividual;
       this.hashvalue = hashvalue;
       this.action = action;
    }
   
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ METHODS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    /*  property: id  */
    /**
    *   Returns the value of property 'id'.   
    */
    public NominatedIndividualId getId() 
    {
        return id;
    }
    
    /**
    *   Sets the value of property 'id'.    
    */
    public void setId( NominatedIndividualId x ) 
    {
        id = x;
    }
    

    /*  property: nominatedIndividual  */
    /**
    *   Returns the value of property 'nominatedIndividual'.   
    */
    public String getNominatedIndividual() 
    {
        return nominatedIndividual;
    }
    
    /**
    *   Sets the value of property 'nominatedIndividual'.    
    */
    public void setNominatedIndividual( String x ) 
    {
        nominatedIndividual = x;
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
            + ", nominatedIndividual=" 
            + nominatedIndividual      
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
            
		if ( !(x instanceof NominatedIndividual) ) 
		    return false;
		    
		NominatedIndividual other = (NominatedIndividual) x; 
		
		return this.id == other.id
		    && this.nominatedIndividual == other.nominatedIndividual
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
            + nominatedIndividual.hashCode()
            + hashvalue.hashCode()
            + action.hashCode();  
            
        return result;
    }   

}


