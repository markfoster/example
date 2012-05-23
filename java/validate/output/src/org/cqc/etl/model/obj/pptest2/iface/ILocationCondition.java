package org.cqc.etl.model.obj.pptest2.iface;
import java.util.Date;
import javax.persistence.Basic;
import org.cqc.etl.model.obj.pptest2.LocationConditionPK;


/** 
 * Object interface mapping for hibernate-handled table: location_condition.
 * @author autogenerated
 */

public interface ILocationCondition {



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
     * Return the value associated with the column: id.
	 * @return A LocationConditionPK object (this.id)
	 */
	LocationConditionPK getId();
	

  
    /**  
     * Set the value related to the column: id.
	 * @param id the id value you wish to set
	 */
	void setId(final LocationConditionPK id);

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
     * Return the value associated with the column: reason.
	 * @return A String object (this.reason)
	 */
	String getReason();
	

  
    /**  
     * Set the value related to the column: reason.
	 * @param reason the reason value you wish to set
	 */
	void setReason(final String reason);

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

    /**
     * Return the value associated with the column: text.
	 * @return A String object (this.text)
	 */
	String getText();
	

  
    /**  
     * Set the value related to the column: text.
	 * @param text the text value you wish to set
	 */
	void setText(final String text);

    /**
     * Return the value associated with the column: type.
	 * @return A String object (this.type)
	 */
	String getType();
	

  
    /**  
     * Set the value related to the column: type.
	 * @param type the type value you wish to set
	 */
	void setType(final String type);

	// end of interface
}