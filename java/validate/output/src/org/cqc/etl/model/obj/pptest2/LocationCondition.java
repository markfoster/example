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
import org.cqc.etl.model.obj.pptest2.iface.ILocationCondition;


/** 
 * Object mapping for hibernate-handled table: location_condition.
 * @author autogenerated
 */

@Entity
@Table(name = "location_condition", catalog = "pptest2")
public class LocationCondition implements Cloneable, Serializable, IPojoGenEntity, ILocationCondition {

	/** Serial Version UID. */
	private static final long serialVersionUID = -559033234L;

	

	/** Field mapping. */
	@Column( name = "action_code", length = 1  )
	private String actionCode;

	/** Field mapping. */
	@Id 
	@Column( name = "condition_id", nullable = false  )
	private LocationConditionPK id;

	/** Field mapping. */
	@Column( name = "last_updated"  )
	private Date lastUpdated;

	/** Field mapping. */
	@Column( length = 715827882  )
	private String reason;

	/** Field mapping. */
	@Column( name = "regulated_activity_number", length = 10  )
	private String regulatedActivityNumber;

	/** Field mapping. */
	@Column( length = 715827882  )
	private String text;

	/** Field mapping. */
	@Column( length = 1  )
	private String type;

	/**
	 * Default constructor, mainly for hibernate use.
	 */
	public LocationCondition() {
		// Default constructor
	} 

	/** Constructor taking a given ID.
	 * @param id to set
	 */
	public LocationCondition(LocationConditionPK id) {
		this.id = id;
	}
	
 


 
	/** Return the type of this class. Useful for when dealing with proxies.
	* @return Defining class.
	*/
	@Transient
	public Class<?> getClassType() {
		return LocationCondition.class;
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
     * Return the value associated with the column: id.
	 * @return A LocationConditionPK object (this.id)
	 */
	@Basic( optional = false )
	@Column( name = "condition_id", nullable = false  )
	public LocationConditionPK getId() {
		return this.id;
		
	}
	

  
    /**  
     * Set the value related to the column: id.
	 * @param id the id value you wish to set
	 */
	public void setId(final LocationConditionPK id) {
		this.id = id;
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
     * Return the value associated with the column: reason.
	 * @return A String object (this.reason)
	 */
	@Basic( optional = true )
	@Column( length = 715827882  )
	public String getReason() {
		return this.reason;
		
	}
	

  
    /**  
     * Set the value related to the column: reason.
	 * @param reason the reason value you wish to set
	 */
	public void setReason(final String reason) {
		this.reason = reason;
	}

    /**
     * Return the value associated with the column: regulatedActivityNumber.
	 * @return A String object (this.regulatedActivityNumber)
	 */
	@Basic( optional = true )
	@Column( name = "regulated_activity_number", length = 10  )
	public String getRegulatedActivityNumber() {
		return this.regulatedActivityNumber;
		
	}
	

  
    /**  
     * Set the value related to the column: regulatedActivityNumber.
	 * @param regulatedActivityNumber the regulatedActivityNumber value you wish to set
	 */
	public void setRegulatedActivityNumber(final String regulatedActivityNumber) {
		this.regulatedActivityNumber = regulatedActivityNumber;
	}

    /**
     * Return the value associated with the column: text.
	 * @return A String object (this.text)
	 */
	@Basic( optional = true )
	@Column( length = 715827882  )
	public String getText() {
		return this.text;
		
	}
	

  
    /**  
     * Set the value related to the column: text.
	 * @param text the text value you wish to set
	 */
	public void setText(final String text) {
		this.text = text;
	}

    /**
     * Return the value associated with the column: type.
	 * @return A String object (this.type)
	 */
	@Basic( optional = true )
	@Column( length = 1  )
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
    * Deep copy.
	* @return cloned object
	* @throws CloneNotSupportedException on error
    */
    @Override
    public LocationCondition clone() throws CloneNotSupportedException {
		
        final LocationCondition copy = (LocationCondition)super.clone();

		copy.setActionCode(this.getActionCode());
		copy.setId(this.getId());
		copy.setLastUpdated(this.getLastUpdated());
		copy.setReason(this.getReason());
		copy.setRegulatedActivityNumber(this.getRegulatedActivityNumber());
		copy.setText(this.getText());
		copy.setType(this.getType());
		return copy;
	}
	


	/** Provides toString implementation.
	 * @see java.lang.Object#toString()
	 * @return String representation of this class.
	 */
	@Override
	public String toString() {
		StringBuffer sb = new StringBuffer();
		
		sb.append("actionCode: " + this.getActionCode() + ", ");
		sb.append("id: " + this.getId() + ", ");
		sb.append("lastUpdated: " + this.getLastUpdated() + ", ");
		sb.append("reason: " + this.getReason() + ", ");
		sb.append("regulatedActivityNumber: " + this.getRegulatedActivityNumber() + ", ");
		sb.append("text: " + this.getText() + ", ");
		sb.append("type: " + this.getType());
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
	
		final LocationCondition that = (LocationCondition) aThat;
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