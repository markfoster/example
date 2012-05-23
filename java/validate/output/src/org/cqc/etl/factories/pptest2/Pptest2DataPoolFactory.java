package org.cqc.etl.factories.pptest2;

import com.felees.hbnpojogen.randomlib.data.dataGeneration.*;
import org.cqc.etl.model.obj.pptest2.*;
import org.springframework.stereotype.Component;

import com.google.common.collect.ArrayListMultimap;
import com.google.common.collect.Multimap;
import java.util.Collection;

/** 
 * DAO factory implementation.
 * @author autogenerated
 */
@Component
public class Pptest2DataPoolFactory {
	/** Table commit order. */
    private static final Multimap<String, String> tableDeps = ArrayListMultimap.create();
	/** DB commit order. */
	private static final String[] commitOrder = new String[]{"ServiceUserBand", "ServiceType", "ReportSummary", "RegisteredManagerCondition", "RegisteredManager", "ProviderRegulatedActivity", "ProviderCondition", "Provider", "Partner", "Outcome", "NominatedIndividual", "LocationRegulatedActivity", "LocationCondition", "Location", "Chapter"};
	static{
		// Store table deps for possible use. 
	}

    /**
     * Data pool factory for Chapter.
     * @return ChapterA Chapter object
     */
    public static Chapter getChapter() {

        Chapter chapter = new Chapter();    
        
        chapter.setActionCode(BasicDataGenerator.generateRandomStringChar(1));
        chapter.setId(getChapterPK());
        chapter.setScore(BasicDataGenerator.generateRandomInt());

        return chapter;
    }

    /**
     * Data pool factory for ChapterPK.
     * @return ChapterPKA ChapterPK object
     */
    public static ChapterPK getChapterPK() {

        ChapterPK chapterPK = new ChapterPK();    
        
        chapterPK.setChapterNumber(BasicDataGenerator.generateRandomString(5));
        chapterPK.setLocationId(BasicDataGenerator.generateRandomString(50));
        chapterPK.setProviderId(BasicDataGenerator.generateRandomString(50));

        return chapterPK;
    }

    /**
     * Data pool factory for Location.
     * @return LocationA Location object
     */
    public static Location getLocation() {

        Location location = new Location();    
        
        location.setAboutLocation(BasicDataGenerator.generateRandomString(715827882));
        location.setActionCode(BasicDataGenerator.generateRandomStringChar(1));
        location.setAddress1(BasicDataGenerator.generateRandomString(200));
        location.setAddress2(BasicDataGenerator.generateRandomString(100));
        location.setAlsoKnownAs(BasicDataGenerator.generateRandomString(100));
        location.setCounty(BasicDataGenerator.generateRandomString(50));
        location.setEmail(BasicDataGenerator.generateRandomString(100));
        location.setFax(BasicDataGenerator.generateRandomString(20));
        location.setId(getLocationPK());
        location.setInProcess(BasicDataGenerator.generateRandomString(1));
        location.setLastUpdated(BasicDataGenerator.generateDate());
        location.setLatitude(BasicDataGenerator.generateRandomDecimal(10, 8));
        location.setLongitude(BasicDataGenerator.generateRandomDecimal(10, 8));
        location.setName(BasicDataGenerator.generateRandomString(100));
        location.setPostcode(BasicDataGenerator.generateRandomString(30));
        location.setSubtype(BasicDataGenerator.generateRandomString(30));
        location.setTelephone(BasicDataGenerator.generateRandomString(20));
        location.setTowncity(BasicDataGenerator.generateRandomString(50));
        location.setType(BasicDataGenerator.generateRandomString(30));
        location.setUnderReviewText(BasicDataGenerator.generateRandomString(255));
        location.setUserExperience(BasicDataGenerator.generateRandomString(715827882));
        location.setWebsite(BasicDataGenerator.generateRandomString(100));

        return location;
    }

    /**
     * Data pool factory for LocationPK.
     * @return LocationPKA LocationPK object
     */
    public static LocationPK getLocationPK() {

        LocationPK locationPK = new LocationPK();    
        
        locationPK.setLocationId(BasicDataGenerator.generateRandomString(50));
        locationPK.setProviderId(BasicDataGenerator.generateRandomString(50));

        return locationPK;
    }

    /**
     * Data pool factory for LocationCondition.
     * @return LocationConditionA LocationCondition object
     */
    public static LocationCondition getLocationCondition() {

        LocationCondition locationCondition = new LocationCondition();    
        
        locationCondition.setActionCode(BasicDataGenerator.generateRandomStringChar(1));
        locationCondition.setId(getLocationConditionPK());
        locationCondition.setLastUpdated(BasicDataGenerator.generateDate());
        locationCondition.setReason(BasicDataGenerator.generateRandomString(715827882));
        locationCondition.setRegulatedActivityNumber(BasicDataGenerator.generateRandomString(10));
        locationCondition.setText(BasicDataGenerator.generateRandomString(715827882));
        locationCondition.setType(BasicDataGenerator.generateRandomStringChar(1));

        return locationCondition;
    }

    /**
     * Data pool factory for LocationConditionPK.
     * @return LocationConditionPKA LocationConditionPK object
     */
    public static LocationConditionPK getLocationConditionPK() {

        LocationConditionPK locationConditionPK = new LocationConditionPK();    
        
        locationConditionPK.setConditionId(BasicDataGenerator.generateRandomString(50));
        locationConditionPK.setLocationId(BasicDataGenerator.generateRandomString(50));
        locationConditionPK.setProviderId(BasicDataGenerator.generateRandomString(50));

        return locationConditionPK;
    }

    /**
     * Data pool factory for LocationRegulatedActivity.
     * @return LocationRegulatedActivityA LocationRegulatedActivity object
     */
    public static LocationRegulatedActivity getLocationRegulatedActivity() {

        LocationRegulatedActivity locationRegulatedActivity = new LocationRegulatedActivity();    
        
        locationRegulatedActivity.setActionCode(BasicDataGenerator.generateRandomStringChar(1));
        locationRegulatedActivity.setId(getLocationRegulatedActivityPK());
        locationRegulatedActivity.setLastUpdated(BasicDataGenerator.generateDate());

        return locationRegulatedActivity;
    }

    /**
     * Data pool factory for LocationRegulatedActivityPK.
     * @return LocationRegulatedActivityPKA LocationRegulatedActivityPK object
     */
    public static LocationRegulatedActivityPK getLocationRegulatedActivityPK() {

        LocationRegulatedActivityPK locationRegulatedActivityPK = new LocationRegulatedActivityPK();    
        
        locationRegulatedActivityPK.setLocationId(BasicDataGenerator.generateRandomString(50));
        locationRegulatedActivityPK.setProviderId(BasicDataGenerator.generateRandomString(50));
        locationRegulatedActivityPK.setRegulatedActivityNumber(BasicDataGenerator.generateRandomString(10));

        return locationRegulatedActivityPK;
    }

    /**
     * Data pool factory for NominatedIndividual.
     * @return NominatedIndividualA NominatedIndividual object
     */
    public static NominatedIndividual getNominatedIndividual() {

        NominatedIndividual nominatedIndividual = new NominatedIndividual();    
        
        nominatedIndividual.setActionCode(BasicDataGenerator.generateRandomStringChar(1));
        nominatedIndividual.setId(getNominatedIndividualPK());
        nominatedIndividual.setName(BasicDataGenerator.generateRandomString(115));

        return nominatedIndividual;
    }

    /**
     * Data pool factory for NominatedIndividualPK.
     * @return NominatedIndividualPKA NominatedIndividualPK object
     */
    public static NominatedIndividualPK getNominatedIndividualPK() {

        NominatedIndividualPK nominatedIndividualPK = new NominatedIndividualPK();    
        
        nominatedIndividualPK.setLocationId(BasicDataGenerator.generateRandomString(50));
        nominatedIndividualPK.setProviderId(BasicDataGenerator.generateRandomString(50));
        nominatedIndividualPK.setRegulatedActivityNumber(BasicDataGenerator.generateRandomString(10));

        return nominatedIndividualPK;
    }

    /**
     * Data pool factory for Outcome.
     * @return OutcomeA Outcome object
     */
    public static Outcome getOutcome() {

        Outcome outcome = new Outcome();    
        
        outcome.setActionCode(BasicDataGenerator.generateRandomStringChar(1));
        outcome.setId(getOutcomePK());
        outcome.setJudgementDate(BasicDataGenerator.generateRandomString(20));
        outcome.setJudgementId(BasicDataGenerator.generateRandomString(30));
        outcome.setJudgementOtherEvidence(BasicDataGenerator.generateRandomString(255));
        outcome.setJudgementReason(BasicDataGenerator.generateRandomString(255));
        outcome.setJudgementScoreId(BasicDataGenerator.generateRandomString(30));
        outcome.setJudgementSummary(BasicDataGenerator.generateRandomString(255));
        outcome.setJudgementUserExperience(BasicDataGenerator.generateRandomString(255));
        outcome.setOutcomeStatementId(BasicDataGenerator.generateRandomString(30));

        return outcome;
    }

    /**
     * Data pool factory for OutcomePK.
     * @return OutcomePKA OutcomePK object
     */
    public static OutcomePK getOutcomePK() {

        OutcomePK outcomePK = new OutcomePK();    
        
        outcomePK.setLocationId(BasicDataGenerator.generateRandomString(30));
        outcomePK.setOutcomeId(BasicDataGenerator.generateRandomString(30));
        outcomePK.setProviderId(BasicDataGenerator.generateRandomString(30));

        return outcomePK;
    }

    /**
     * Data pool factory for Partner.
     * @return PartnerA Partner object
     */
    public static Partner getPartner() {

        Partner partner = new Partner();    
        
        partner.setActionCode(BasicDataGenerator.generateRandomStringChar(1));
        partner.setId(getPartnerPK());
        partner.setLastUpdated(BasicDataGenerator.generateDate());
        partner.setName(BasicDataGenerator.generateRandomString(115));

        return partner;
    }

    /**
     * Data pool factory for PartnerPK.
     * @return PartnerPKA PartnerPK object
     */
    public static PartnerPK getPartnerPK() {

        PartnerPK partnerPK = new PartnerPK();    
        
        partnerPK.setPartnerId(BasicDataGenerator.generateRandomString(50));
        partnerPK.setProviderId(BasicDataGenerator.generateRandomString(50));

        return partnerPK;
    }

    /**
     * Data pool factory for Provider.
     * @return ProviderA Provider object
     */
    public static Provider getProvider() {

        Provider provider = new Provider();    
        
        provider.setActionCode(BasicDataGenerator.generateRandomStringChar(1));
        provider.setAddress1(BasicDataGenerator.generateRandomString(200));
        provider.setAddress2(BasicDataGenerator.generateRandomString(100));
        provider.setAlsoKnownAs(BasicDataGenerator.generateRandomString(100));
        provider.setCounty(BasicDataGenerator.generateRandomString(255));
        provider.setEmail(BasicDataGenerator.generateRandomString(50));
        provider.setFax(BasicDataGenerator.generateRandomString(40));
        provider.setId(BasicDataGenerator.generateRandomString(50));
        provider.setInProcess(BasicDataGenerator.generateRandomString(1));
        provider.setIsPartnership(BasicDataGenerator.generateRandomString(1));
        provider.setLatitude(BasicDataGenerator.generateRandomDecimal(10, 8));
        provider.setLongitude(BasicDataGenerator.generateRandomDecimal(10, 8));
        provider.setName(BasicDataGenerator.generateRandomString(100));
        provider.setPostcode(BasicDataGenerator.generateRandomString(30));
        provider.setRegion(BasicDataGenerator.generateRandomString(50));
        provider.setSegmentation(BasicDataGenerator.generateRandomString(50));
        provider.setSubtype(BasicDataGenerator.generateRandomString(30));
        provider.setTelephone(BasicDataGenerator.generateRandomString(20));
        provider.setTowncity(BasicDataGenerator.generateRandomString(255));
        provider.setType(BasicDataGenerator.generateRandomString(50));
        provider.setUnderReviewText(BasicDataGenerator.generateRandomString(255));
        provider.setUserExperience(BasicDataGenerator.generateRandomString(50));
        provider.setWebsite(BasicDataGenerator.generateRandomString(100));

        return provider;
    }

    /**
     * Data pool factory for ProviderCondition.
     * @return ProviderConditionA ProviderCondition object
     */
    public static ProviderCondition getProviderCondition() {

        ProviderCondition providerCondition = new ProviderCondition();    
        
        providerCondition.setActionCode(BasicDataGenerator.generateRandomStringChar(1));
        providerCondition.setId(getProviderConditionPK());
        providerCondition.setLastUpdated(BasicDataGenerator.generateDate());
        providerCondition.setReason(BasicDataGenerator.generateRandomString(255));
        providerCondition.setRegulatedActivityNumber(BasicDataGenerator.generateRandomString(10));
        providerCondition.setText(BasicDataGenerator.generateRandomString(715827882));

        return providerCondition;
    }

    /**
     * Data pool factory for ProviderConditionPK.
     * @return ProviderConditionPKA ProviderConditionPK object
     */
    public static ProviderConditionPK getProviderConditionPK() {

        ProviderConditionPK providerConditionPK = new ProviderConditionPK();    
        
        providerConditionPK.setConditionId(BasicDataGenerator.generateRandomString(50));
        providerConditionPK.setLocationId(BasicDataGenerator.generateRandomString(50));
        providerConditionPK.setProviderId(BasicDataGenerator.generateRandomString(50));

        return providerConditionPK;
    }

    /**
     * Data pool factory for ProviderRegulatedActivity.
     * @return ProviderRegulatedActivityA ProviderRegulatedActivity object
     */
    public static ProviderRegulatedActivity getProviderRegulatedActivity() {

        ProviderRegulatedActivity providerRegulatedActivity = new ProviderRegulatedActivity();    
        
        providerRegulatedActivity.setActionCode(BasicDataGenerator.generateRandomStringChar(1));
        providerRegulatedActivity.setId(getProviderRegulatedActivityPK());
        providerRegulatedActivity.setLastUpdated(BasicDataGenerator.generateDate());

        return providerRegulatedActivity;
    }

    /**
     * Data pool factory for ProviderRegulatedActivityPK.
     * @return ProviderRegulatedActivityPKA ProviderRegulatedActivityPK object
     */
    public static ProviderRegulatedActivityPK getProviderRegulatedActivityPK() {

        ProviderRegulatedActivityPK providerRegulatedActivityPK = new ProviderRegulatedActivityPK();    
        
        providerRegulatedActivityPK.setProviderId(BasicDataGenerator.generateRandomString(30));
        providerRegulatedActivityPK.setRegulatedActivityNumber(BasicDataGenerator.generateRandomString(10));

        return providerRegulatedActivityPK;
    }

    /**
     * Data pool factory for RegisteredManager.
     * @return RegisteredManagerA RegisteredManager object
     */
    public static RegisteredManager getRegisteredManager() {

        RegisteredManager registeredManager = new RegisteredManager();    
        
        registeredManager.setActionCode(BasicDataGenerator.generateRandomStringChar(1));
        registeredManager.setId(getRegisteredManagerPK());
        registeredManager.setLastUpdated(BasicDataGenerator.generateDate());
        registeredManager.setManagerCondition(BasicDataGenerator.generateRandomString(255));
        registeredManager.setName(BasicDataGenerator.generateRandomString(115));
        registeredManager.setRegisteredManagerId(BasicDataGenerator.generateRandomString(50));
        registeredManager.setRegulatedActivityNumber(BasicDataGenerator.generateRandomString(10));

        return registeredManager;
    }

    /**
     * Data pool factory for RegisteredManagerPK.
     * @return RegisteredManagerPKA RegisteredManagerPK object
     */
    public static RegisteredManagerPK getRegisteredManagerPK() {

        RegisteredManagerPK registeredManagerPK = new RegisteredManagerPK();    
        
        registeredManagerPK.setLocationId(BasicDataGenerator.generateRandomString(50));
        registeredManagerPK.setProviderId(BasicDataGenerator.generateRandomString(50));

        return registeredManagerPK;
    }

    /**
     * Data pool factory for RegisteredManagerCondition.
     * @return RegisteredManagerConditionA RegisteredManagerCondition object
     */
    public static RegisteredManagerCondition getRegisteredManagerCondition() {

        RegisteredManagerCondition registeredManagerCondition = new RegisteredManagerCondition();    
        
        registeredManagerCondition.setActionCode(BasicDataGenerator.generateRandomStringChar(1));
        registeredManagerCondition.setConditionId(BasicDataGenerator.generateRandomString(50));
        registeredManagerCondition.setConditionText(BasicDataGenerator.generateRandomString(715827882));
        registeredManagerCondition.setId(getRegisteredManagerConditionPK());
        registeredManagerCondition.setLastUpdated(BasicDataGenerator.generateDate());
        registeredManagerCondition.setRegisteredManagerId(BasicDataGenerator.generateRandomString(50));
        registeredManagerCondition.setRegulatedActivityNumber(BasicDataGenerator.generateRandomString(10));

        return registeredManagerCondition;
    }

    /**
     * Data pool factory for RegisteredManagerConditionPK.
     * @return RegisteredManagerConditionPKA RegisteredManagerConditionPK object
     */
    public static RegisteredManagerConditionPK getRegisteredManagerConditionPK() {

        RegisteredManagerConditionPK registeredManagerConditionPK = new RegisteredManagerConditionPK();    
        
        registeredManagerConditionPK.setLocationId(BasicDataGenerator.generateRandomString(50));
        registeredManagerConditionPK.setProviderId(BasicDataGenerator.generateRandomString(50));

        return registeredManagerConditionPK;
    }

    /**
     * Data pool factory for ReportSummary.
     * @return ReportSummaryA ReportSummary object
     */
    public static ReportSummary getReportSummary() {

        ReportSummary reportSummary = new ReportSummary();    
        
        reportSummary.setActionCode(BasicDataGenerator.generateRandomStringChar(1));
        reportSummary.setId(getReportSummaryPK());
        reportSummary.setLastUpdated(BasicDataGenerator.generateDate());
        reportSummary.setText(BasicDataGenerator.generateRandomString(255));

        return reportSummary;
    }

    /**
     * Data pool factory for ReportSummaryPK.
     * @return ReportSummaryPKA ReportSummaryPK object
     */
    public static ReportSummaryPK getReportSummaryPK() {

        ReportSummaryPK reportSummaryPK = new ReportSummaryPK();    
        
        reportSummaryPK.setLocationId(BasicDataGenerator.generateRandomString(50));
        reportSummaryPK.setProviderId(BasicDataGenerator.generateRandomString(50));
        reportSummaryPK.setReviewDate(BasicDataGenerator.generateDate());

        return reportSummaryPK;
    }

    /**
     * Data pool factory for ServiceType.
     * @return ServiceTypeA ServiceType object
     */
    public static ServiceType getServiceType() {

        ServiceType serviceType = new ServiceType();    
        
        serviceType.setHashvalue(BasicDataGenerator.generateRandomString(32));
        serviceType.setId(getServiceTypePK());

        return serviceType;
    }

    /**
     * Data pool factory for ServiceTypePK.
     * @return ServiceTypePKA ServiceTypePK object
     */
    public static ServiceTypePK getServiceTypePK() {

        ServiceTypePK serviceTypePK = new ServiceTypePK();    
        
        serviceTypePK.setLocationId(BasicDataGenerator.generateRandomString(30));
        serviceTypePK.setProviderId(BasicDataGenerator.generateRandomString(30));
        serviceTypePK.setServiceTypeId(BasicDataGenerator.generateRandomString(30));

        return serviceTypePK;
    }

    /**
     * Data pool factory for ServiceUserBand.
     * @return ServiceUserBandA ServiceUserBand object
     */
    public static ServiceUserBand getServiceUserBand() {

        ServiceUserBand serviceUserBand = new ServiceUserBand();    
        
        serviceUserBand.setActionCode(BasicDataGenerator.generateRandomStringChar(1));
        serviceUserBand.setId(getServiceUserBandPK());
        serviceUserBand.setLastUpdated(BasicDataGenerator.generateDate());

        return serviceUserBand;
    }

    /**
     * Data pool factory for ServiceUserBandPK.
     * @return ServiceUserBandPKA ServiceUserBandPK object
     */
    public static ServiceUserBandPK getServiceUserBandPK() {

        ServiceUserBandPK serviceUserBandPK = new ServiceUserBandPK();    
        
        serviceUserBandPK.setLocationId(BasicDataGenerator.generateRandomString(50));
        serviceUserBandPK.setProviderId(BasicDataGenerator.generateRandomString(50));
        serviceUserBandPK.setServiceUserBandId(BasicDataGenerator.generateRandomString(50));

        return serviceUserBandPK;
    }
    /** Returns the commit order of this database. 
	 * Useful for iterating through the classes for deletion in the right order. 
	 * @return String[] list of classes
	 */
	public static String[] getDBCommitOrder() {
		return commitOrder;
	}
	
	/**
	 * @param className classname to return
	 * @return the tabledeps for the given class name
	 */
	public static Collection<String> getTabledeps(String className) {
		return tableDeps.get(className);
	}
	
}