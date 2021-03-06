package org.cqc.etl.model.obj.pptest2.iface;
import java.util.Date;
import javax.persistence.Basic;
import org.cqc.etl.model.obj.pptest2.RegisteredManagerConditionPK;


/** 
 * Object interface mapping for hibernate-handled table: registered_manager_condition.
 * @author autogenerated
 */

public interface IRegisteredManagerCondition {



    /**
     * Return the value associated with the column: actionCode.
	 * @return A String object (this.actionCode)
	 */
	String getActionCode();
	

  
    /**  
     * Set the value related to the column: actionCode.
	 * @param actionCode the actionCode value you wish to set
	 */
	void setActionCode(final String actionCode);

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
     * Return the value associated with the column: conditionText.
	 * @return A String object (this.conditionText)
	 */
	String getConditionText();
	

  
    /**  
     * Set the value related to the column: conditionText.
	 * @param conditionText the conditionText value you wish to set
	 */
	void setConditionText(final String conditionText);

    /**
     * Return the value associated with the column: id.
	 * @return A RegisteredManagerConditionPK object (this.id)
	 */
	RegisteredManagerConditionPK getId();
	

  
    /**  
     * Set the value related to the column: id.
	 * @param id the id value you wish to set
	 */
	void setId(final RegisteredManagerConditionPK id);

    /**
     * Return the value associated with the column: lastUpdated.
	 * @return A Date object (this.lastUpdated)
	 */
	Date getLastUpdated();
	

  
    /**  
     * Set the value related to the column: lastUpdated.
	 * @param lastUpdated the lastUpdated value you wish to set
	 */
	void setLastUpdated(final Date lastUpdated);

    /**
     * Return the value associated with the column: registeredManagerId.
	 * @return A String object (this.registeredManagerId)
	 */
	String getRegisteredManagerId();
	

  
    /**  
     * Set the value related to the column: registeredManagerId.
	 * @param registeredManagerId the registeredManagerId value you wish to set
	 */
	void setRegisteredManagerId(final String registeredManagerId);

    /**
     * Return the value associated with the column: regulatedActivityNumber.
	 * @return A String object (this.regulatedActivityNumber)
	 */
	String getRegulatedActivityNumber();
	

  
    /**  
     * Set the value related to the column: regulatedActivityNumber.
	 * @param regulatedActivityNumber the regulatedActivityNumber value you wish to set
	 */
	void setRegulatedActivityNumber(final String regulatedActivityNumber);

	// end of interface
}