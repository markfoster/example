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
import org.cqc.etl.model.obj.pptest2.iface.IServiceUserBand;


/** 
 * Object mapping for hibernate-handled table: service_user_band.
 * @author autogenerated
 */

@Entity
@Table(name = "service_user_band", catalog = "pptest2")
public class ServiceUserBand implements Cloneable, Serializable, IPojoGenEntity, IServiceUserBand {

	/** Serial Version UID. */
	private static final long serialVersionUID = -559033200L;

	

	/** Field mapping. */
	@Column( name = "action_code", length = 1  )
	private String actionCode;

	/** Field mapping. */
	@Id 
	@Column( name = "location_id", nullable = false  )
	private ServiceUserBandPK id;

	/** Field mapping. */
	@Column( name = "last_updated"  )
	private Date lastUpdated;

	/**
	 * Default constructor, mainly for hibernate use.
	 */
	public ServiceUserBand() {
		// Default constructor
	} 

	/** Constructor taking a given ID.
	 * @param id to set
	 */
	public ServiceUserBand(ServiceUserBandPK id) {
		this.id = id;
	}
	
 


 
	/** Return the type of this class. Useful for when dealing with proxies.
	* @return Defining class.
	*/
	@Transient
	public Class<?> getClassType() {
		return ServiceUserBand.class;
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
	 * @return A ServiceUserBandPK object (this.id)
	 */
	@Basic( optional = false )
	@Column( name = "location_id", nullable = false  )
	public ServiceUserBandPK getId() {
		return this.id;
		
	}
	

  
    /**  
     * Set the value related to the column: id.
	 * @param id the id value you wish to set
	 */
	public void setId(final ServiceUserBandPK id) {
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
    * Deep copy.
	* @return cloned object
	* @throws CloneNotSupportedException on error
    */
    @Override
    public ServiceUserBand clone() throws CloneNotSupportedException {
		
        final ServiceUserBand copy = (ServiceUserBand)super.clone();

		copy.setActionCode(this.getActionCode());
		copy.setId(this.getId());
		copy.setLastUpdated(this.getLastUpdated());
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
		sb.append("lastUpdated: " + this.getLastUpdated());
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
	
		final ServiceUserBand that = (ServiceUserBand) aThat;
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
