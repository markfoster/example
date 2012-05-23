package org.cqc.etl.model.obj.pptest2;

import com.felees.hbnpojogen.persistence.IPojoGenEntity;
import java.io.Serializable;
import javax.persistence.Basic;
import javax.persistence.Column;
import javax.persistence.Embeddable;
import javax.persistence.Transient;
import org.cqc.etl.model.obj.pptest2.iface.IOutcomePK;


/** 
 * Object mapping for hibernate-handled table: outcome.
 * @author autogenerated
 */

@Embeddable
public class OutcomePK implements Cloneable, Serializable,  IOutcomePK {

	/** Serial Version UID. */
	private static final long serialVersionUID = -559033223L;

	

	/** Field mapping. */
	@Column( name = "location_id", nullable = false, length = 30  )
	private String locationId;

	/** Field mapping. */
	@Column( name = "outcome_id", nullable = false, length = 30  )
	private String outcomeId;

	/** Field mapping. */
	@Column( name = "provider_id", nullable = false, length = 30  )
	private String providerId;

 


 
	/** Return the type of this class. Useful for when dealing with proxies.
	* @return Defining class.
	*/
	@Transient
	public Class<?> getClassType() {
		return OutcomePK.class;
	}
 

    /**
     * Return the value associated with the column: locationId.
	 * @return A String object (this.locationId)
	 */
	public String getLocationId() {
		return this.locationId;
		
	}
	

  
    /**  
     * Set the value related to the column: locationId.
	 * @param locationId the locationId value you wish to set
	 */
	public void setLocationId(final String locationId) {
		this.locationId = locationId;
	}

    /**
     * Return the value associated with the column: outcomeId.
	 * @return A String object (this.outcomeId)
	 */
	public String getOutcomeId() {
		return this.outcomeId;
		
	}
	

  
    /**  
     * Set the value related to the column: outcomeId.
	 * @param outcomeId the outcomeId value you wish to set
	 */
	public void setOutcomeId(final String outcomeId) {
		this.outcomeId = outcomeId;
	}

    /**
     * Return the value associated with the column: providerId.
	 * @return A String object (this.providerId)
	 */
	public String getProviderId() {
		return this.providerId;
		
	}
	

  
    /**  
     * Set the value related to the column: providerId.
	 * @param providerId the providerId value you wish to set
	 */
	public void setProviderId(final String providerId) {
		this.providerId = providerId;
	}


   /**
    * Deep copy.
	* @return cloned object
	* @throws CloneNotSupportedException on error
    */
    @Override
    public OutcomePK clone() throws CloneNotSupportedException {
		
        final OutcomePK copy = (OutcomePK)super.clone();

		copy.setLocationId(this.getLocationId());
		copy.setOutcomeId(this.getOutcomeId());
		copy.setProviderId(this.getProviderId());
		return copy;
	}
	


	/** Provides toString implementation.
	 * @see java.lang.Object#toString()
	 * @return String representation of this class.
	 */
	@Override
	public String toString() {
		StringBuffer sb = new StringBuffer();
		
		sb.append("locationId: " + this.getLocationId() + ", ");
		sb.append("outcomeId: " + this.getOutcomeId() + ", ");
		sb.append("providerId: " + this.getProviderId());
		return sb.toString();		
	}


	/** Equals implementation. 
	 * @see java.lang.Object#equals(java.lang.Object)
	 * @param aThat Object to compare with
	 * @return true/false
	 */
	@Override
	public boolean equals(final Object aThat) {
		Object proxyThat = aThat;
		
		if ( this == aThat ) {
			 return true;
		}

		if (aThat == null)  {
			 return false;
		}
		
		final OutcomePK that; 
		try {
			that = (OutcomePK) proxyThat;
			if ( !(that.getClassType().equals(this.getClassType()))){
				return false;
			}
		} catch (org.hibernate.ObjectNotFoundException e) {
				return false;
		} catch (ClassCastException e) {
				return false;
		}
		
		
		boolean result = true;
		result = result && (((getLocationId() == null) && (that.getLocationId() == null)) || (getLocationId() != null && getLocationId().equals(that.getLocationId())));
		result = result && (((getOutcomeId() == null) && (that.getOutcomeId() == null)) || (getOutcomeId() != null && getOutcomeId().equals(that.getOutcomeId())));
		result = result && (((getProviderId() == null) && (that.getProviderId() == null)) || (getProviderId() != null && getProviderId().equals(that.getProviderId())));
		return result;
	}
	
	/** Calculate the hashcode.
	 * @see java.lang.Object#hashCode()
	 * @return a calculated number
	 */
	@Override
	public int hashCode() {
	int hash = 0;
		hash = hash + getLocationId().hashCode();
		hash = hash + getOutcomeId().hashCode();
		hash = hash + getProviderId().hashCode();
	return hash;
	}
	

	
}