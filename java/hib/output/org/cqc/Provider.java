/*
*   $HeadURL:$
*   Created: 24-Apr-2012 11:57:32                       
*   Copyright (c) 2010, Matt Harrison. All rights reserved.
*/
package org.cqc;


import java.math.BigDecimal;

/**
*   Data access object representing a Provider.
*
*   @author matth
*   @version $Rev: 2 $
*/
public class Provider  implements java.io.Serializable
{
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ FIELDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    private String providerId;
    
    private String providerName;
    
    private String inProcess;
    
    private String providerType;
    
    private String alsoKnownAs;
    
    private String address1;
    
    private String address2;
    
    private String towncity;
    
    private String county;
    
    private String postcode;
    
    private BigDecimal latitude;
    
    private BigDecimal longitude;
    
    private String typeInfo1;
    
    private String typeInfo2;
    
    private String underReviewText;
    
    private String telephone;
    
    private String email;
    
    private String website;
    
    private String fax;
    
    private String isPartnership;
    
    private String hashvalue;
    
    private Character action;


    //~~~~~~~~~~~~~~~~~~~~~~~ CONSTRUCTORS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    /** Default constructor. */ 
    public Provider() 
    {
    }



    /** Full constructor. 
    *
    *   @param providerName
    *   @param inProcess
    *   @param providerType
    *   @param alsoKnownAs
    *   @param address1
    *   @param address2
    *   @param towncity
    *   @param county
    *   @param postcode
    *   @param latitude
    *   @param longitude
    *   @param typeInfo1
    *   @param typeInfo2
    *   @param underReviewText
    *   @param telephone
    *   @param email
    *   @param website
    *   @param fax
    *   @param isPartnership
    *   @param hashvalue
    *   @param action
    */ 
    public Provider( String providerName, String inProcess, String providerType, String alsoKnownAs, String address1, String address2, String towncity, String county, String postcode, BigDecimal latitude, BigDecimal longitude, String typeInfo1, String typeInfo2, String underReviewText, String telephone, String email, String website, String fax, String isPartnership, String hashvalue, Character action ) 
    {
       this.providerName = providerName;
       this.inProcess = inProcess;
       this.providerType = providerType;
       this.alsoKnownAs = alsoKnownAs;
       this.address1 = address1;
       this.address2 = address2;
       this.towncity = towncity;
       this.county = county;
       this.postcode = postcode;
       this.latitude = latitude;
       this.longitude = longitude;
       this.typeInfo1 = typeInfo1;
       this.typeInfo2 = typeInfo2;
       this.underReviewText = underReviewText;
       this.telephone = telephone;
       this.email = email;
       this.website = website;
       this.fax = fax;
       this.isPartnership = isPartnership;
       this.hashvalue = hashvalue;
       this.action = action;
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
    

    /*  property: providerName  */
    /**
    *   Returns the value of property 'providerName'.   
    */
    public String getProviderName() 
    {
        return providerName;
    }
    
    /**
    *   Sets the value of property 'providerName'.    
    */
    public void setProviderName( String x ) 
    {
        providerName = x;
    }
    

    /*  property: inProcess  */
    /**
    *   Returns the value of property 'inProcess'.   
    */
    public String getInProcess() 
    {
        return inProcess;
    }
    
    /**
    *   Sets the value of property 'inProcess'.    
    */
    public void setInProcess( String x ) 
    {
        inProcess = x;
    }
    

    /*  property: providerType  */
    /**
    *   Returns the value of property 'providerType'.   
    */
    public String getProviderType() 
    {
        return providerType;
    }
    
    /**
    *   Sets the value of property 'providerType'.    
    */
    public void setProviderType( String x ) 
    {
        providerType = x;
    }
    

    /*  property: alsoKnownAs  */
    /**
    *   Returns the value of property 'alsoKnownAs'.   
    */
    public String getAlsoKnownAs() 
    {
        return alsoKnownAs;
    }
    
    /**
    *   Sets the value of property 'alsoKnownAs'.    
    */
    public void setAlsoKnownAs( String x ) 
    {
        alsoKnownAs = x;
    }
    

    /*  property: address1  */
    /**
    *   Returns the value of property 'address1'.   
    */
    public String getAddress1() 
    {
        return address1;
    }
    
    /**
    *   Sets the value of property 'address1'.    
    */
    public void setAddress1( String x ) 
    {
        address1 = x;
    }
    

    /*  property: address2  */
    /**
    *   Returns the value of property 'address2'.   
    */
    public String getAddress2() 
    {
        return address2;
    }
    
    /**
    *   Sets the value of property 'address2'.    
    */
    public void setAddress2( String x ) 
    {
        address2 = x;
    }
    

    /*  property: towncity  */
    /**
    *   Returns the value of property 'towncity'.   
    */
    public String getTowncity() 
    {
        return towncity;
    }
    
    /**
    *   Sets the value of property 'towncity'.    
    */
    public void setTowncity( String x ) 
    {
        towncity = x;
    }
    

    /*  property: county  */
    /**
    *   Returns the value of property 'county'.   
    */
    public String getCounty() 
    {
        return county;
    }
    
    /**
    *   Sets the value of property 'county'.    
    */
    public void setCounty( String x ) 
    {
        county = x;
    }
    

    /*  property: postcode  */
    /**
    *   Returns the value of property 'postcode'.   
    */
    public String getPostcode() 
    {
        return postcode;
    }
    
    /**
    *   Sets the value of property 'postcode'.    
    */
    public void setPostcode( String x ) 
    {
        postcode = x;
    }
    

    /*  property: latitude  */
    /**
    *   Returns the value of property 'latitude'.   
    */
    public BigDecimal getLatitude() 
    {
        return latitude;
    }
    
    /**
    *   Sets the value of property 'latitude'.    
    */
    public void setLatitude( BigDecimal x ) 
    {
        latitude = x;
    }
    

    /*  property: longitude  */
    /**
    *   Returns the value of property 'longitude'.   
    */
    public BigDecimal getLongitude() 
    {
        return longitude;
    }
    
    /**
    *   Sets the value of property 'longitude'.    
    */
    public void setLongitude( BigDecimal x ) 
    {
        longitude = x;
    }
    

    /*  property: typeInfo1  */
    /**
    *   Returns the value of property 'typeInfo1'.   
    */
    public String getTypeInfo1() 
    {
        return typeInfo1;
    }
    
    /**
    *   Sets the value of property 'typeInfo1'.    
    */
    public void setTypeInfo1( String x ) 
    {
        typeInfo1 = x;
    }
    

    /*  property: typeInfo2  */
    /**
    *   Returns the value of property 'typeInfo2'.   
    */
    public String getTypeInfo2() 
    {
        return typeInfo2;
    }
    
    /**
    *   Sets the value of property 'typeInfo2'.    
    */
    public void setTypeInfo2( String x ) 
    {
        typeInfo2 = x;
    }
    

    /*  property: underReviewText  */
    /**
    *   Returns the value of property 'underReviewText'.   
    */
    public String getUnderReviewText() 
    {
        return underReviewText;
    }
    
    /**
    *   Sets the value of property 'underReviewText'.    
    */
    public void setUnderReviewText( String x ) 
    {
        underReviewText = x;
    }
    

    /*  property: telephone  */
    /**
    *   Returns the value of property 'telephone'.   
    */
    public String getTelephone() 
    {
        return telephone;
    }
    
    /**
    *   Sets the value of property 'telephone'.    
    */
    public void setTelephone( String x ) 
    {
        telephone = x;
    }
    

    /*  property: email  */
    /**
    *   Returns the value of property 'email'.   
    */
    public String getEmail() 
    {
        return email;
    }
    
    /**
    *   Sets the value of property 'email'.    
    */
    public void setEmail( String x ) 
    {
        email = x;
    }
    

    /*  property: website  */
    /**
    *   Returns the value of property 'website'.   
    */
    public String getWebsite() 
    {
        return website;
    }
    
    /**
    *   Sets the value of property 'website'.    
    */
    public void setWebsite( String x ) 
    {
        website = x;
    }
    

    /*  property: fax  */
    /**
    *   Returns the value of property 'fax'.   
    */
    public String getFax() 
    {
        return fax;
    }
    
    /**
    *   Sets the value of property 'fax'.    
    */
    public void setFax( String x ) 
    {
        fax = x;
    }
    

    /*  property: isPartnership  */
    /**
    *   Returns the value of property 'isPartnership'.   
    */
    public String getIsPartnership() 
    {
        return isPartnership;
    }
    
    /**
    *   Sets the value of property 'isPartnership'.    
    */
    public void setIsPartnership( String x ) 
    {
        isPartnership = x;
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
            + ": providerId=" 
            + providerId      
            + ", providerName=" 
            + providerName      
            + ", inProcess=" 
            + inProcess      
            + ", providerType=" 
            + providerType      
            + ", alsoKnownAs=" 
            + alsoKnownAs      
            + ", address1=" 
            + address1      
            + ", address2=" 
            + address2      
            + ", towncity=" 
            + towncity      
            + ", county=" 
            + county      
            + ", postcode=" 
            + postcode      
            + ", latitude=" 
            + latitude      
            + ", longitude=" 
            + longitude      
            + ", typeInfo1=" 
            + typeInfo1      
            + ", typeInfo2=" 
            + typeInfo2      
            + ", underReviewText=" 
            + underReviewText      
            + ", telephone=" 
            + telephone      
            + ", email=" 
            + email      
            + ", website=" 
            + website      
            + ", fax=" 
            + fax      
            + ", isPartnership=" 
            + isPartnership      
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
            
		if ( !(x instanceof Provider) ) 
		    return false;
		    
		Provider other = (Provider) x; 
		
		return this.providerId == other.providerId
		    && this.providerName == other.providerName
		    && this.inProcess == other.inProcess
		    && this.providerType == other.providerType
		    && this.alsoKnownAs == other.alsoKnownAs
		    && this.address1 == other.address1
		    && this.address2 == other.address2
		    && this.towncity == other.towncity
		    && this.county == other.county
		    && this.postcode == other.postcode
		    && this.latitude == other.latitude
		    && this.longitude == other.longitude
		    && this.typeInfo1 == other.typeInfo1
		    && this.typeInfo2 == other.typeInfo2
		    && this.underReviewText == other.underReviewText
		    && this.telephone == other.telephone
		    && this.email == other.email
		    && this.website == other.website
		    && this.fax == other.fax
		    && this.isPartnership == other.isPartnership
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
            + providerId.hashCode()
            + providerName.hashCode()
            + inProcess.hashCode()
            + providerType.hashCode()
            + alsoKnownAs.hashCode()
            + address1.hashCode()
            + address2.hashCode()
            + towncity.hashCode()
            + county.hashCode()
            + postcode.hashCode()
            + latitude.hashCode()
            + longitude.hashCode()
            + typeInfo1.hashCode()
            + typeInfo2.hashCode()
            + underReviewText.hashCode()
            + telephone.hashCode()
            + email.hashCode()
            + website.hashCode()
            + fax.hashCode()
            + isPartnership.hashCode()
            + hashvalue.hashCode()
            + action.hashCode();  
            
        return result;
    }   

}


