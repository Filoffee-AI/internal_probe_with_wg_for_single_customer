Readme.txt
 
-------------------------------------------------------------------
This file outlines changes since the last release of MIBs.
 
It is very strongly recommended that you load and compile ALL of
the MIBs provided.
 
Please load the 'hpicfOid.mib' before loading the other specific
MIBs.  This is due to the fact that the 'hpicfOid.mib' is the
parent MIB to most of the HP device specific MIBs.
-------------------------------------------------------------------
 
		hpicfArpThrottle.mib
		   -modified objects
			hpicfArpThrottleThreshold
		   -new objects
			hpicfArpThrottleDenylistAgingTime
			hpicfArpThrottleStatsNumClientsInDenylist
 
 
		hpicfDevConf.mib
		   -new objects
			hpSwitchAllowlistMacAddress
			hpSwitchAllowlistMacEntry
			hpSwitchAllowlistMacTable
			hpSwitchAllowlistRowStatus
 
 
		hpicfGenericVlan.mib
		   -modified objects
			hpicfDot1qTpFdbInstalledTime
 
 
		hpicfHighAvailability.mib
		   -modified objects
			hpicfHAMgmtModuleBackUpState
 
 
		hpicfIpRoute.mib
		   -modified objects
			hpicfIpStaticRouteFwdIfIndex
			hpicfIpStaticRouteLogging
			hpicfIpStaticRouteType
 
 
		hpicfOpenFlow.mib
		   -modified objects
			hpicfOpenFlowInstanceControllerRole
 
 
		hpicfSmartLink.mib
		   -modified objects
			hpicfSmartLinkExtendedGroupEntry
			hpicfSmartLinkGroupEntry
			hpicfSmartLinkGroupPreemptionMode
			hpicfSmartLinkPortStateChangeNotification
		   -new objects
			hpicfSmartLinkGroupPrimaryPort
			hpicfSmartLinkGroupPrimaryPortState
			hpicfSmartLinkGroupSecondaryPort
			hpicfSmartLinkGroupSecondaryPortState
			hpicfSmartLinkPortStateChangeNotification1
			hpicfSmartLinkPrimaryFlushPktLastUpdate
			hpicfSmartLinkPrimaryFlushPktTx
			hpicfSmartLinkSecondaryFlushPktLastUpdate
			hpicfSmartLinkSecondaryFlushPktTx
 
 
		hpicfTC.mib
		   -modified objects
		        HpInetCidrRouteState
		
		
		hpicfTunneledNode.mib
		   -new objects
		        hpicfTunneledNodeWolVIDList


		hpicfUrpf.mib
		   -new objects
			hpicfUrpfConfigAllowlistAclName
			hpicfUrpfConfigHasAllowlistAcl
 
 
		hpicfVrrp.mib
		   -modified objects
			hpicfVrrpNonstop
			hpicfVrrpOperEntry
			hpicfVrrpRespondToPing
			hpicfVrrpStatsNearFailovers
			hpicfVrrpVrControl
			hpicfVrrpVrRespondToPing
		   -new objects
			hpicfVrrpVrMainPreempt
 
 
		hpicfVrrpv3.mib
		   -modified objects
			hpicfVrrpv3Nonstop
			hpicfVrrpv3RespondToPing
			hpicfVrrpv3StatsNearFailovers
			hpicfVrrpv3VrBfdIPAddr
			hpicfVrrpv3VrControl
			hpicfVrrpv3VrRespondToPing
 
 
		hpicfXrrp.mib
		   -modified objects
			hpicfXrrpInstanceAdvertiseInterval
			hpicfXrrpInstanceOperState
			hpicfXrrpStatsInstancePriorityZeroPktsRcvd
			hpicfXrrpStatsRcEntry
			hpicfXrrpStatsRcOperState
			hpicfXrrpTrapAuthFailure
			hpicfXrrpTrapCntl
		   -new objects
			hpicfXrrpStatsRcBecomeMain
			hpicfXrrpStatsRcMainRouterTime
 
 
		hpStack.mib
		   -modified objects
			hpStackMemberState
 
 
		hpSwitchConfig.mib
		   -modified objects
			hpSwitchPortVgMode
 
 
