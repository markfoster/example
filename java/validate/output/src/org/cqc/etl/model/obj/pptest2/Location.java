package org.cqc.etl.model.obj.pptest2;

import com.felees.hbnpojogen.persistence.IPojoGenEntity;
import java.io.Serializable;
import java.util.Date;
import javax.persistence.Basic;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.persistence.Transient;
import org.cqc.etl.model.obj.pptest2.iface.ILocation;


/** 
 * Object mapping for hibernate-handled table: location.
 * @author autogenerated
 */

@Entity
@Table(name = "location", catalog = "pptest2")
public class Location implements Cloneable, Serializable, IPojoGenEntity, ILocation {

	/** Serial Version UID. */
	private static final long serialVersionUID = -559033237L;

	

	/** Field mapping. */
	@Column( name = "about_location", length = 715827882  )
	private String aboutLocation;

	/** Field mapping. */
	@Column( name = "action_code", length = 1  )
	private String actionCode;

	/** Field mapping. */
	@Column( length = 200  )
	private String address1;

	/** Field mapping. */
	@Column( length = 100  )
	private String address2;

	/** Field mapping. */
	@Column( name = "also_known_as", length = 100  )
	private String alsoKnownAs;

	/** Field mapping. */
	@Column( length = 50  )
	private String county;

	/** Field mapping. */
	@Column( length = 100  )
	private String email;

	/** Field mapping. */
	@Column( length = 20  )
	private String fax;

	/** Field mapping. */
	@Id 
	@Column( name = "location_id", nullable = false  )
	private LocationPK id;

	/** Field mapping. */
	@Column( name = "in_process", length = 1  )
	private String inProcess;

	/** Field mapping. */
	@Column( name = "last_updated"  )
	private Date lastUpdated;

	/** Field mapping. */
	private java.math.BigDecimal latitude;

	/** Field mapping. */
	private java.math.BigDecimal longitude;

	/** Field mapping. */
	@Column( length = 100  )
	private String name;

	/** Field mapping. */
	@Column( length = 30  )
	private String postcode;

	/** Field mapping. */
	@Column( length = 30  )
	private String subtype;

	/** Field mapping. */
	@Column( length = 20  )
	private String telephone;

	/** Field mapping. */
	@Column( length = 50  )
	private String towncity;

	/** Field mapping. */
	@Column( length = 30  )
	private String type;

	/** Field mapping. */
	@Column( name = "under_review_text", length = 255  )
	private String underReviewText;

	/** Field mapping. */
	@Column( name = "user_experience", length = 715827882  )
	private String userExperience;

	/** Field mapping. */
	@Column( length = 100  )
	private String website;

	/**
	 * Default constructor, mainly for hibernate use.
	 */
	public Location() {
		// Default constructor
	} 

	/** Constructor taking a given ID.
	 * @param id to set
	 */
	public Location(LocationPK id) {
		this.id = id;
	}
	
 


 
	/** Return the type of this class. Useful for when dealing with proxies.
	* @return Defining class.
	*/
	@Transient
	public Class<?> getClassType() {
		return Location.class;
	}
 

    /**
     * Return the value associated with the column: aboutLocation.
	 * @return A String object (this.aboutLocation)
	 */
	@Basic( optional = true )
	@Column( name = "about_location", length = 715827882  )
	public String getAboutLocation() {
		return this.aboutLocation;
		
	}
	

  
    /**  
     * Set the value related to the column: aboutLocation.
	 * @param aboutLocation the aboutLocation value you wish to set
	 */
	public void setAboutLocation(final String aboutLocation) {
		this.aboutLocation = aboutLocation;
	}

    /**
     * Return the value associated with the column: actionCode.
	 * @return A String object (this.actionCode)
	 */
	@Basic( optional = true )
	@Column( name = "action_code", length = 1  )
	public String getActionCode() {
		return this.actionCode;
		
	}
	

  
    /**  
     * Set the value related to the column: actionCode.
	 * @param actionCode the actionCode value you wish to set
	 */
	public void setActionCode(final String actionCode) {
		this.actionCode = actionCode;
	}

    /**
     * Return the value associated with the column: address1.
	 * @return A String object (this.address1)
	 */
	@Basic( optional = true )
	@Column( length = 200  )
	public String getAddress1() {
		return this.address1;
		
	}
	

  
    /**  
     * Set the value related to the column: address1.
	 * @param address1 the address1 value you wish to set
	 */
	public void setAddress1(final String address1) {
		this.address1 = address1;
	}

    /**
     * Return the value associated with the column: address2.
	 * @return A String object (this.address2)
	 */
	@Basic( optional = true )
	@Column( length = 100  )
	public String getAddress2() {
		return this.address2;
		
	}
	

  
    /**  
     * Set the value related to the column: address2.
	 * @param address2 the address2 value you wish to set
	 */
	public void setAddress2(final String address2) {
		this.address2 = address2;
	}

    /**
     * Return the value associated with the column: alsoKnownAs.
	 * @return A String object (this.alsoKnownAs)
	 */
	@Basic( optional = true )
	@Column( name = "also_known_as", length = 100  )
	public String getAlsoKnownAs() {
		return this.alsoKnownAs;
		
	}
	

  
    /**  
     * Set the value related to the column: alsoKnownAs.
	 * @param alsoKnownAs the alsoKnownAs value you wish to set
	 */
	public void setAlsoKnownAs(final String alsoKnownAs) {
		this.alsoKnownAs = alsoKnownAs;
	}

    /**
     * Return the value associated with the column: county.
	 * @return A String object (this.county)
	 */
	@Basic( optional = true )
	@Column( length = 50  )
	public String getCounty() {
		return this.county;
		
	}
	

  
    /**  
     * Set the value related to the column: county.
	 * @param county the county value you wish to set
	 */
	public void setCounty(final String county) {
		this.county = county;
	}

    /**
     * Return the value associated with the column: email.
	 * @return A String object (this.email)
	 */
	@Basic( optional = true )
	@Column( length = 100  )
	public String getEmail() {
		return this.email;
		
	}
	

  
    /**  
     * Set the value related to the column: email.
	 * @param email the email value you wish to set
	 */
	public void setEmail(final String email) {
		this.email = email;
	}

    /**
     * Return the value associated with the column: fax.
	 * @return A String object (this.fax)
	 */
	@Basic( optional = true )
	@Column( length = 20  )
	public String getFax() {
		return this.fax;
		
	}
	

  
    /**  
     * Set the value related to the column: fax.
	 * @param fax the fax value you wish to set
	 */
	public void setFax(final String fax) {
		this.fax = fax;
	}

    /**
     * Return the value associated with the column: id.
	 * @return A LocationPK object (this.id)
	 */
	@Basic( optional = false )
	@Column( name = "location_id", nullable = false  )
	public LocationPK getId() {
		return this.id;
		
	}
	

  
    /**  
     * Set the value related to the column: id.
	 * @param id the id value you wish to set
	 */
	public void setId(final LocationPK id) {
		this.id = id;
	}

    /**
     * Return the value associated with the column: inProcess.
	 * @return A String object (this.inProcess)
	 */
	@Basic( optional = true )
	@Column( name = "in_process", length = 1  )
	public String getInProcess() {
		return this.inProcess;
		
	}
	

  
    /**  
     * Set the value related to the column: inProcess.
	 * @param inProcess the inProcess value you wish to set
	 */
	public void setInProcess(final String inProcess) {
		this.inProcess = inProcess;
	}

    /**
     * Return the value associated with the column: lastUpdated.
	 * @return A Date object (this.lastUpdated)
	 */
	@Basic( optional = true )
	@Column( name = "last_updated"  )
	public Date getLastUpdated() {
		return this.lastUpdated;
		
	}
	

  
    /**  
     * Set the value related to the column: lastUpdated.
	 * @param lastUpdated the lastUpdated value you wish to set
	 */
	public void setLastUpdated(final Date lastUpdated) {
		this.lastUpdated = lastUpdated;
	}

    /**
     * Return the value associated with the column: latitude.
	 * @return A java.math.BigDecimal object (this.latitude)
	 */
	public java.math.BigDecimal getLatitude() {
		return this.latitude;
		
	}
	

  
    /**  
     * Set the value related to the column: latitude.
	 * @param latitude the latitude value you wish to set
	 */
	public void setLatitude(final java.math.BigDecimal latitude) {
		this.latitude = latitude;
	}

    /**
     * Return the value associated with the column: longitude.
	 * @return A java.math.BigDecimal object (this.longitude)
	 */
	public java.math.BigDecimal getLongitude() {
		return this.longitude;
		
	}
	

  
    /**  
     * Set the value related to the column: longitude.
	 * @param longitude the longitude value you wish to set
	 */
	public void setLongitude(final java.math.BigDecimal longitude) {
		this.longitude = longitude;
	}

    /**
     * Return the value associated with the column: name.
	 * @return A String object (this.name)
	 */
	@Basic( optional = true )
	@Column( length = 100  )
	public String getName() {
		return this.name;
		
	}
	

  
    /**  
     * Set the value related to the column: name.
	 * @param name the name value you wish to set
	 */
	public void setName(final String name) {
		this.name = name;
	}

    /**
     * Return the value associated with the column: postcode.
	 * @return A String object (this.postcode)
	 */
	@Basic( optional = true )
	@Column( length = 30  )
	public String getPostcode() {
		return this.postcode;
		
	}
	

  
    /**  
     * Set the value related to the column: postcode.
	 * @param postcode the postcode value you wish to set
	 */
	public void setPostcode(final String postcode) {
		this.postcode = postcode;
	}

    /**
     * Return the value associated with the column: subtype.
	 * @return A String object (this.subtype)
	 */
	@Basic( optional = true )
	@Column( length = 30  )
	public String getSubtype() {
		return this.subtype;
		
	}
	

  
    /**  
     * Set the value related to the column: subtype.
	 * @param subtype the subtype value you wish to set
	 */
	public void setSubtype(final String subtype) {
		this.subtype = subtype;
	}

    /**
     * Return the value associated with the column: telephone.
	 * @return A String object (this.telephone)
	 */
	@Basic( optional = true )
	@Column( length = 20  )
	public String getTelephone() {
		return this.telephone;
		
	}
	

  
    /**  
     * Set the value related to the column: telephone.
	 * @param telephone the telephone value you wish to set
	 */
	public void setTelephone(final String telephone) {
		this.telephone = telephone;
	}

    /**
     * Return the value associated with the column: towncity.
	 * @return A String object (this.towncity)
	 */
	@Basic( optional = true )
	@Column( length = 50  )
	public String getTowncity() {
		return this.towncity;
		
	}
	

  
    /**  
     * Set the value related to the column: towncity.
	 * @param towncity the towncity value you wish to set
	 */
	public void setTowncity(final String towncity) {
		this.towncity = towncity;
	}

    /**
     * Return the value associated with the column: type.
	 * @return A String object (this.type)
	 */
	@Basic( optional = true )
	@Column( length = 30  )
	public String getType() {
		return this.type;
		
	}
	

  
    /**  
     * Set the value related to the column: type.
	 * @param type the type value you wish to set
	 */
	public void setType(final String type) {
		this.type = type;
	}

    /**
     * Return the value associated with the column: underReviewText.
	 * @return A String object (this.underReviewText)
	 */
	@Basic( optional = true )
	@Column( name = "under_review_text", length = 255  )
	public String getUnderReviewText() {
		return this.underReviewText;
		
	}
	

  
    /**  
     * Set the value related to the column: underReviewText.
	 * @param underReviewText the underReviewText value you wish to set
	 */
	public void setUnderReviewText(final String underReviewText) {
		this.underReviewText = underReviewText;
	}

    /**
     * Return the value associated with the column: userExperience.
	 * @return A String object (this.userExperience)
	 */
	@Basic( optional = true )
	@Column( name = "user_experience", length = 715827882  )
	public String getUserExperience() {
		return this.userExperience;
		
	}
	

  
    /**  
     * Set the value related to the column: userExperience.
	 * @param userExperience the userExperience value you wish to set
	 */
	public void setUserExperience(final String userExperience) {
		this.userExperience = userExperience;
	}

    /**
     * Return the value associated with the column: website.
	 * @return A String object (this.website)
	 */
	@Basic( optional = true )
	@Column( length = 100  )
	public String getWebsite() {
		return this.website;
		
	}
	

  
    /**  
     * Set the value related to the column: website.
	 * @param website the website value you wish to set
	 */
	public void setWebsite(final String website) {
		this.website = website;
	}


   /**
    * Deep copy.
	* @return cloned object
	* @throws CloneNotSupportedException on error
    */
    @Override
    public Location clone() throws CloneNotSupportedException {
		
        final Location copy = (Location)super.clone();

		copy.setAboutLocation(this.getAboutLocation());
		copy.setActionCode(this.getActionCode());
		copy.setAddress1(this.getAddress1());
		copy.setAddress2(this.getAddress2());
		copy.setAlsoKnownAs(this.getAlsoKnownAs());
		copy.setCounty(this.getCounty());
		copy.setEmail(this.getEmail());
		copy.setFax(this.getFax());
		copy.setId(this.getId());
		copy.setInProcess(this.getInProcess());
		copy.setLastUpdated(this.getLastUpdated());
		copy.setLatitude(this.getLatitude());
		copy.setLongitude(this.getLongitude());
		copy.setName(this.getName());
		copy.setPostcode(this.getPostcode());
		copy.setSubtype(this.getSubtype());
		copy.setTelephone(this.getTelephone());
		copy.setTowncity(this.getTowncity());
		copy.setType(this.getType());
		copy.setUnderReviewText(this.getUnderReviewText());
		copy.setUserExperience(this.getUserExperience());
		copy.setWebsite(this.getWebsite());
		return copy;
	}
	


	/** Provides toString implementation.
	 * @see java.lang.Object#toString()
	 * @return String representation of this class.
	 */
	@Override
	public String toString() {
		StringBuffer sb = new StringBuffer();
		
		sb.append("aboutLocation: " + this.getAboutLocation() + ", ");
		sb.append("actionCode: " + this.getActionCode() + ", ");
		sb.append("address1: " + this.getAddress1() + ", ");
		sb.append("address2: " + this.getAddress2() + ", ");
		sb.append("alsoKnownAs: " + this.getAlsoKnownAs() + ", ");
		sb.append("county: " + this.getCounty() + ", ");
		sb.append("email: " + this.getEmail() + ", ");
		sb.append("fax: " + this.getFax() + ", ");
		sb.append("id: " + this.getId() + ", ");
		sb.append("inProcess: " + this.getInProcess() + ", ");
		sb.append("lastUpdated: " + this.getLastUpdated() + ", ");
		sb.append("latitude: " + this.getLatitude() + ", ");
		sb.append("longitude: " + this.getLongitude() + ", ");
		sb.append("name: " + this.getName() + ", ");
		sb.append("postcode: " + this.getPostcode() + ", ");
		sb.append("subtype: " + this.getSubtype() + ", ");
		sb.append("telephone: " + this.getTelephone() + ", ");
		sb.append("towncity: " + this.getTowncity() + ", ");
		sb.append("type: " + this.getType() + ", ");
		sb.append("underReviewText: " + this.getUnderReviewText() + ", ");
		sb.append("userExperience: " + this.getUserExperience() + ", ");
		sb.append("website: " + this.getWebsite());
		return sb.toString();		
	}


	/** Equals implementation. 
	 * @see java.lang.Object#equals(java.lang.Object)
	 * @param aThat Object to compare with
	 * @return true/false
	 */
	@Override
	public boolean equals(final Object aThat) {
		if ( this == aThat ) {
			 return true;
		}

		if ((aThat == null) || ( !(aThat.getClass().equals(this.getClass())))) {
			 return false;
		}
	
		final Location that = (Location) aThat;
		return this.getId().equals(that.getId());
	}
	
	/** Calculate the hashcode.
	 * @see java.lang.Object#hashCode()
	 * @return a calculated number
	 */
	@Override
	public int hashCode() {
		return getId().hashCode();
	}
	

	
}
