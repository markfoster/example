package org.cqc.etl.model.obj.pptest2;

import com.felees.hbnpojogen.persistence.IPojoGenEntity;
import java.io.Serializable;
import javax.persistence.Basic;
import javax.persistence.Column;
import javax.persistence.Embeddable;
import javax.persistence.Transient;
import org.cqc.etl.model.obj.pptest2.iface.IProviderRegulatedActivityPK;


/** 
 * Object mapping for hibernate-handled table: provider_regulated_activity.
 * @author autogenerated
 */

@Embeddable
public class ProviderRegulatedActivityPK implements Cloneable, Serializable,  IProviderRegulatedActivityPK {

	/** Serial Version UID. */
	private static final long serialVersionUID = -559033213L;

	

	/** Field mapping. */
	@Column( name = "provider_id", nullable = false, length = 30  )
	private String providerId;

	/** Field mapping. */
	@Column( name = "regulated_activity_number", nullable = false, length = 10  )
	private String regulatedActivityNumber;

 


 
	/** Return the type of this class. Useful for when dealing with proxies.
	* @return Defining class.
	*/
	@Transient
	public Class<?> getClassType() {
		return ProviderRegulatedActivityPK.class;
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
     * Return the value associated with the column: regulatedActivityNumber.
	 * @return A String object (this.regulatedActivityNumber)
	 */
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
    public ProviderRegulatedActivityPK clone() throws CloneNotSupportedException {
		
        final ProviderRegulatedActivityPK copy = (ProviderRegulatedActivityPK)super.clone();

		copy.setProviderId(this.getProviderId());
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
		
		sb.append("providerId: " + this.getProviderId() + ", ");
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
		Object proxyThat = aThat;
		
		if ( this == aThat ) {
			 return true;
		}

		if (aThat == null)  {
			 return false;
		}
		
		final ProviderRegulatedActivityPK that; 
		try {
			that = (ProviderRegulatedActivityPK) proxyThat;
			if ( !(that.getClassType().equals(this.getClassType()))){
				return false;
			}
		} catch (org.hibernate.ObjectNotFoundException e) {
				return false;
		} catch (ClassCastException e) {
				return false;
		}
		
		
		boolean result = true;
		result = result && (((getProviderId() == null) && (that.getProviderId() == null)) || (getProviderId() != null && getProviderId().equals(that.getProviderId())));
		result = result && (((getRegulatedActivityNumber() == null) && (that.getRegulatedActivityNumber() == null)) || (getRegulatedActivityNumber() != null && getRegulatedActivityNumber().equals(that.getRegulatedActivityNumber())));
		return result;
	}
	
	/** Calculate the hashcode.
	 * @see java.lang.Object#hashCode()
	 * @return a calculated number
	 */
	@Override
	public int hashCode() {
	int hash = 0;
		hash = hash + getProviderId().hashCode();
		hash = hash + getRegulatedActivityNumber().hashCode();
	return hash;
	}
	

	
}