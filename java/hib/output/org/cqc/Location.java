/*
*   $HeadURL:$
*   Created: 24-Apr-2012 11:57:32                       
*   Copyright (c) 2010, Matt Harrison. All rights reserved.
*/
package org.cqc;


import java.math.BigDecimal;

/**
*   Data access object representing a Location.
*
*   @author matth
*   @version $Rev: 2 $
*/
public class Location  implements java.io.Serializable
{
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ FIELDS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    private LocationId id;
    
    private String locationName;
    
    private String inProcess;
    
    private String locationType;
    
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
    
    private String telephone;
    
    private String email;
    
    private String website;
    
    private String fax;
    
    private String underReviewText;
    
    private String locationUserExperience;
    
    private String locationLicenseInformation;
    
    private String locationStatementDate;
    
    private String locationStatementId;
    
    private String hashvalue;
    
    private Character action;


    //~~~~~~~~~~~~~~~~~~~~~~~ CONSTRUCTORS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    /** Default constructor. */ 
    public Location() 
    {
    }


    /** 
    *   Minimal constructor. 
    *
    *   @param id
    */ 
    public Location( LocationId id ) 
    {
        this.id = id;
    }


    /** Full constructor. 
    *
    *   @param id
    *   @param locationName
    *   @param inProcess
    *   @param locationType
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
    *   @param telephone
    *   @param email
    *   @param website
    *   @param fax
    *   @param underReviewText
    *   @param locationUserExperience
    *   @param locationLicenseInformation
    *   @param locationStatementDate
    *   @param locationStatementId
    *   @param hashvalue
    *   @param action
    */ 
    public Location( LocationId id, String locationName, String inProcess, String locationType, String alsoKnownAs, String address1, String address2, String towncity, String county, String postcode, BigDecimal latitude, BigDecimal longitude, String typeInfo1, String typeInfo2, String telephone, String email, String website, String fax, String underReviewText, String locationUserExperience, String locationLicenseInformation, String locationStatementDate, String locationStatementId, String hashvalue, Character action ) 
    {
       this.id = id;
       this.locationName = locationName;
       this.inProcess = inProcess;
       this.locationType = locationType;
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
       this.telephone = telephone;
       this.email = email;
       this.website = website;
       this.fax = fax;
       this.underReviewText = underReviewText;
       this.locationUserExperience = locationUserExperience;
       this.locationLicenseInformation = locationLicenseInformation;
       this.locationStatementDate = locationStatementDate;
       this.locationStatementId = locationStatementId;
       this.hashvalue = hashvalue;
       this.action = action;
    }
   
    //~~~~~~~~~~~~~~~~~~~~~~~~~~ METHODS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    /*  property: id  */
    /**
    *   Returns the value of property 'id'.   
    */
    public LocationId getId() 
    {
        return id;
    }
    
    /**
    *   Sets the value of property 'id'.    
    */
    public void setId( LocationId x ) 
    {
        id = x;
    }
    

    /*  property: locationName  */
    /**
    *   Returns the value of property 'locationName'.   
    */
    public String getLocationName() 
    {
        return locationName;
    }
    
    /**
    *   Sets the value of property 'locationName'.    
    */
    public void setLocationName( String x ) 
    {
        locationName = x;
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
    

    /*  property: locationType  */
    /**
    *   Returns the value of property 'locationType'.   
    */
    public String getLocationType() 
    {
        return locationType;
    }
    
    /**
    *   Sets the value of property 'locationType'.    
    */
    public void setLocationType( String x ) 
    {
        locationType = x;
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
    

    /*  property: locationUserExperience  */
    /**
    *   Returns the value of property 'locationUserExperience'.   
    */
    public String getLocationUserExperience() 
    {
        return locationUserExperience;
    }
    
    /**
    *   Sets the value of property 'locationUserExperience'.    
    */
    public void setLocationUserExperience( String x ) 
    {
        locationUserExperience = x;
    }
    

    /*  property: locationLicenseInformation  */
    /**
    *   Returns the value of property 'locationLicenseInformation'.   
    */
    public String getLocationLicenseInformation() 
    {
        return locationLicenseInformation;
    }
    
    /**
    *   Sets the value of property 'locationLicenseInformation'.    
    */
    public void setLocationLicenseInformation( String x ) 
    {
        locationLicenseInformation = x;
    }
    

    /*  property: locationStatementDate  */
    /**
    *   Returns the value of property 'locationStatementDate'.   
    */
    public String getLocationStatementDate() 
    {
        return locationStatementDate;
    }
    
    /**
    *   Sets the value of property 'locationStatementDate'.    
    */
    public void setLocationStatementDate( String x ) 
    {
        locationStatementDate = x;
    }
    

    /*  property: locationStatementId  */
    /**
    *   Returns the value of property 'locationStatementId'.   
    */
    public String getLocationStatementId() 
    {
        return locationStatementId;
    }
    
    /**
    *   Sets the value of property 'locationStatementId'.    
    */
    public void setLocationStatementId( String x ) 
    {
        locationStatementId = x;
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
            + ", locationName=" 
            + locationName      
            + ", inProcess=" 
            + inProcess      
            + ", locationType=" 
            + locationType      
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
            + ", telephone=" 
            + telephone      
            + ", email=" 
            + email      
            + ", website=" 
            + website      
            + ", fax=" 
            + fax      
            + ", underReviewText=" 
            + underReviewText      
            + ", locationUserExperience=" 
            + locationUserExperience      
            + ", locationLicenseInformation=" 
            + locationLicenseInformation      
            + ", locationStatementDate=" 
            + locationStatementDate      
            + ", locationStatementId=" 
            + locationStatementId      
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
            
		if ( !(x instanceof Location) ) 
		    return false;
		    
		Location other = (Location) x; 
		
		return this.id == other.id
		    && this.locationName == other.locationName
		    && this.inProcess == other.inProcess
		    && this.locationType == other.locationType
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
		    && this.telephone == other.telephone
		    && this.email == other.email
		    && this.website == other.website
		    && this.fax == other.fax
		    && this.underReviewText == other.underReviewText
		    && this.locationUserExperience == other.locationUserExperience
		    && this.locationLicenseInformation == other.locationLicenseInformation
		    && this.locationStatementDate == other.locationStatementDate
		    && this.locationStatementId == other.locationStatementId
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
            + locationName.hashCode()
            + inProcess.hashCode()
            + locationType.hashCode()
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
            + telephone.hashCode()
            + email.hashCode()
            + website.hashCode()
            + fax.hashCode()
            + underReviewText.hashCode()
            + locationUserExperience.hashCode()
            + locationLicenseInformation.hashCode()
            + locationStatementDate.hashCode()
            + locationStatementId.hashCode()
            + hashvalue.hashCode()
            + action.hashCode();  
            
        return result;
    }   

}


