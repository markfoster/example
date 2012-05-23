package org.cqc.etl.model.obj.pptest2.iface;
import javax.persistence.Basic;


/** 
 * Object interface mapping for hibernate-handled table: provider_condition.
 * @author autogenerated
 */

public interface IProviderConditionPK {



    /**
     * Return the value associated with the column: conditionId.
	 * @return A String object (this.conditionId)
	 */
	String getConditionId();
	

  
    /**  
     * Set the value related to the column: conditionId.
	 * @param conditionId the conditionId value you wish to set
	 */
	void setConditionId(final String conditionId);

    /**
     * Return the value associated with the column: locationId.
	 * @return A String object (this.locationId)
	 */
	String getLocationId();
	

  
    /**  
     * Set the value related to the column: locationId.
	 * @param locationId the locationId value you wish to set
	 */
	void setLocationId(final String locationId);

    /**
     * Return the value associated with the column: providerId.
	 * @return A String object (this.providerId)
	 */
	String getProviderId();
	

  
    /**  
     * Set the value related to the column: providerId.
	 * @param providerId the providerId value you wish to set
	 */
	void setProviderId(final String providerId);

	// end of interface
}