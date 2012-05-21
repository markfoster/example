/*
*   $HeadURL:$
*   Created: 24-Apr-2012 11:57:32                       
*   Copyright (c) 2010, Matt Harrison. All rights reserved.
*/
package org.cqc;



/**
*   Data access object representing a Chapter.
*
*   @author matth
*   @version $Rev: 2 $
*/
public class Chapter  implements java.io.Serializable
{
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ FIELDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    private ChapterId id;
    
    private Integer chapterScore;
    
    private String hashvalue;
    
    private Character action;


    //~~~~~~~~~~~~~~~~~~~~~~~ CONSTRUCTORS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    /** Default constructor. */ 
    public Chapter() 
    {
    }


    /** 
    *   Minimal constructor. 
    *
    *   @param id
    */ 
    public Chapter( ChapterId id ) 
    {
        this.id = id;
    }


    /** Full constructor. 
    *
    *   @param id
    *   @param chapterScore
    *   @param hashvalue
    *   @param action
    */ 
    public Chapter( ChapterId id, Integer chapterScore, String hashvalue, Character action ) 
    {
       this.id = id;
       this.chapterScore = chapterScore;
       this.hashvalue = hashvalue;
       this.action = action;
    }
   
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ METHODS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    /*  property: id  */
    /**
    *   Returns the value of property 'id'.   
    */
    public ChapterId getId() 
    {
        return id;
    }
    
    /**
    *   Sets the value of property 'id'.    
    */
    public void setId( ChapterId x ) 
    {
        id = x;
    }
    

    /*  property: chapterScore  */
    /**
    *   Returns the value of property 'chapterScore'.   
    */
    public Integer getChapterScore() 
    {
        return chapterScore;
    }
    
    /**
    *   Sets the value of property 'chapterScore'.    
    */
    public void setChapterScore( Integer x ) 
    {
        chapterScore = x;
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
            + ", chapterScore=" 
            + chapterScore      
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
            
		if ( !(x instanceof Chapter) ) 
		    return false;
		    
		Chapter other = (Chapter) x; 
		
		return this.id == other.id
		    && this.chapterScore == other.chapterScore
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
            + chapterScore.hashCode()
            + hashvalue.hashCode()
            + action.hashCode();  
            
        return result;
    }   

}


