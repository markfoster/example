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
import org.cqc.etl.model.obj.pptest2.iface.IRegisteredManager;


/** 
 * Object mapping for hibernate-handled table: registered_manager.
 * @author autogenerated
 */

@Entity
@Table(name = "registered_manager", catalog = "pptest2")
public class RegisteredManager implements Cloneable, Serializable, IPojoGenEntity, IRegisteredManager {

	/** Serial Version UID. */
	private static final long serialVersionUID = -559033212L;

	

	/** Field mapping. */
	@Column( name = "action_code", length = 1  )
	private String actionCode;

	/** Field mapping. */
	@Id 
	@Column( name = "location_id", nullable = false  )
	private RegisteredManagerPK id;

	/** Field mapping. */
	@Column( name = "last_updated"  )
	private Date lastUpdated;

	/** Field mapping. */
	@Column( name = "manager_condition", length = 255  )
	private String managerCondition;

	/** Field mapping. */
	@Column( length = 115  )
	private String name;

	/** Field mapping. */
	@Column( name = "registered_manager_id", length = 50  )
	private String registeredManagerId;

	/** Field mapping. */
	@Column( name = "regulated_activity_number", length = 10  )
	private String regulatedActivityNumber;

	/**
	 * Default constructor, mainly for hibernate use.
	 */
	public RegisteredManager() {
		// Default constructor
	} 

	/** Constructor taking a given ID.
	 * @param id to set
	 */
	public RegisteredManager(RegisteredManagerPK id) {
		this.id = id;
	}
	
 


 
	/** Return the type of this class. Useful for when dealing with proxies.
	* @return Defining class.
	*/
	@Transient
	public Class<?> getClassType() {
		return RegisteredManager.class;
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
	 * @return A RegisteredManagerPK object (this.id)
	 */
	@Basic( optional = false )
	@Column( name = "location_id", nullable = false  )
	public RegisteredManagerPK getId() {
		return this.id;
		
	}
	

  
    /**  
     * Set the value related to the column: id.
	 * @param id the id value you wish to set
	 */
	public void setId(final RegisteredManagerPK id) {
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
     * Return the value associated with the column: managerCondition.
	 * @return A String object (this.managerCondition)
	 */
	@Basic( optional = true )
	@Column( name = "manager_condition", length = 255  )
	public String getManagerCondition() {
		return this.managerCondition;
		
	}
	

  
    /**  
     * Set the value related to the column: managerCondition.
	 * @param managerCondition the managerCondition value you wish to set
	 */
	public void setManagerCondition(final String managerCondition) {
		this.managerCondition = managerCondition;
	}

    /**
     * Return the value associated with the column: name.
	 * @return A String object (this.name)
	 */
	@Basic( optional = true )
	@Column( length = 115  )
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
     * Return the value associated with the column: registeredManagerId.
	 * @return A String object (this.registeredManagerId)
	 */
	@Basic( optional = true )
	@Column( name = "registered_manager_id", length = 50  )
	public String getRegisteredManagerId() {
		return this.registeredManagerId;
		
	}
	

  
    /**  
     * Set the value related to the column: registeredManagerId.
	 * @param registeredManagerId the registeredManagerId value you wish to set
	 */
	public void setRegisteredManagerId(final String registeredManagerId) {
		this.registeredManagerId = registeredManagerId;
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
    * Deep copy.
	* @return cloned object
	* @throws CloneNotSupportedException on error
    */
    @Override
    public RegisteredManager clone() throws CloneNotSupportedException {
		
        final RegisteredManager copy = (RegisteredManager)super.clone();

		copy.setActionCode(this.getActionCode());
		copy.setId(this.getId());
		copy.setLastUpdated(this.getLastUpdated());
		copy.setManagerCondition(this.getManagerCondition());
		copy.setName(this.getName());
		copy.setRegisteredManagerId(this.getRegisteredManagerId());
		copy.setRegulatedActivityNumber(this.getRegulatedActivityNumber());
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
		sb.append("managerCondition: " + this.getManagerCondition() + ", ");
		sb.append("name: " + this.getName() + ", ");
		sb.append("registeredManagerId: " + this.getRegisteredManagerId() + ", ");
		sb.append("regulatedActivityNumber: " + this.getRegulatedActivityNumber());
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
	
		final RegisteredManager that = (RegisteredManager) aThat;
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
