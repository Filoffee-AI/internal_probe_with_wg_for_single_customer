<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>ARUBAWIRED-VSF-MIB</title>
<META HTTP-EQUIV="CONTENT-TYPE" CONTENT="text/html; charset=UTF-8">
<META HTTP-EQUIV="CACHE-CONTROL" CONTENT="ALL">
<META NAME="ROBOTS" CONTENT="ALL">
<META NAME="DESCRIPTION" CONTENT="www.circitor.fr: ARUBAWIRED-VSF-MIB">
<META NAME="COPYRIGHT" CONTENT="Copyright &copy; 2007 - 2022 - Circitor">
<META NAME="KEYWORDS" CONTENT="SNMP, MIB, ARUBAWIRED-VSF-MIB">
<META NAME="AUTHOR" CONTENT="Circitor">
<link rel="stylesheet" href="/Mibs/Style_mib.css" type="text/css">
</head>
<body>
<div id="body_global">
<div id="body_header">
<img src="/Mibs/logo.png" alt="" width="100%">
</div>
<div id="body_main">
<h1>ARUBAWIRED-VSF-MIB</h1>
File: <a href="../../Mib/A/ARUBAWIRED-VSF-MIB.mib">ARUBAWIRED-VSF-MIB.mib</a> (17396 bytes)
<h2><u>Imported modules</u></h2>
<table width="100%" border="1">
<tr>
<td width="33%"><a href="../../Html/S/SNMPv2-SMI.php">SNMPv2-SMI</a></td>
<td width="33%"><a href="../../Html/S/SNMPv2-CONF.php">SNMPv2-CONF</a></td>
<td width="33%"><a href="../../Html/S/SNMPv2-TC.php">SNMPv2-TC</a></td>
</tr>
<tr>
<td width="33%"><a href="../../Html/Q/Q-BRIDGE-MIB.php">Q-BRIDGE-MIB</a></td>
<td width="33%"><a href="../../Html/A/ARUBAWIRED-NETWORKING-OID.php">ARUBAWIRED-NETWORKING-OID</a></td>
<td width="33%"></td>
</table>
<h2><u>Imported symbols</u></h2>
<table width="100%" border="1">
<tr>
<td width="33%"><a href="../../Html/S/SNMPv2-SMI.php#MODULE-IDENTITY">MODULE-IDENTITY</a></td>
<td width="33%"><a href="../../Html/S/SNMPv2-SMI.php#OBJECT-TYPE">OBJECT-TYPE</a></td>
<td width="33%"><a href="../../Html/S/SNMPv2-SMI.php#Integer32">Integer32</a></td>
</tr>
<tr>
<td width="33%"><a href="../../Html/S/SNMPv2-SMI.php#NOTIFICATION-TYPE">NOTIFICATION-TYPE</a></td>
<td width="33%"><a href="../../Html/S/SNMPv2-SMI.php#TimeTicks">TimeTicks</a></td>
<td width="33%"><a href="../../Html/S/SNMPv2-CONF.php#MODULE-COMPLIANCE">MODULE-COMPLIANCE</a></td>
</tr>
<tr>
<td width="33%"><a href="../../Html/S/SNMPv2-CONF.php#OBJECT-GROUP">OBJECT-GROUP</a></td>
<td width="33%"><a href="../../Html/S/SNMPv2-CONF.php#NOTIFICATION-GROUP">NOTIFICATION-GROUP</a></td>
<td width="33%"><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></td>
</tr>
<tr>
<td width="33%"><a href="../../Html/S/SNMPv2-TC.php#TruthValue">TruthValue</a></td>
<td width="33%"><a href="../../Html/S/SNMPv2-TC.php#MacAddress">MacAddress</a></td>
<td width="33%"><a href="../../Html/Q/Q-BRIDGE-MIB.php#PortList">PortList</a></td>
</tr>
<tr>
<td width="33%"><a href="../../Html/A/ARUBAWIRED-NETWORKING-OID.php#wndFeatures">wndFeatures</a></td>
<td width="33%"></td>
<td width="33%"></td>
</table>
<h2><u>Defined Types</u></h2>
<table id=ArubaWiredVsfMemberEntry width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#ArubaWiredVsfMemberEntry">ArubaWiredVsfMemberEntry</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>&nbsp;</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>SEQUENCE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfMemberIndex</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-SMI.php#Integer32">Integer32</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfMemberRole</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfMemberStatus</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfMemberPartNumber</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfMemberMacAddr</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#MacAddress">MacAddress</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfMemberProductName</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfMemberSerialNum</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfMemberBootImage</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfMemberCpuUtil</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>INTEGER</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfMemberMemoryUtil</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>INTEGER</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfMemberBootTime</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-SMI.php#TimeTicks">TimeTicks</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfMemberBootRomVersion</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfMemberTotalMemory</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>INTEGER</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfMemberCurrentUsage</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>INTEGER</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
</table>
<br>
<table id=ArubaWiredVsfLinkEntry width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#ArubaWiredVsfLinkEntry">ArubaWiredVsfLinkEntry</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>&nbsp;</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>SEQUENCE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfLinkMemberId</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>INTEGER</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfLinkId</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>INTEGER</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfLinkOperStatus</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfLinkPeerMemberId</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>INTEGER</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfLinkPeerLinkId</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>INTEGER</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>arubaWiredVsfLinkPortList</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/Q/Q-BRIDGE-MIB.php#PortList">PortList</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
</table>
<br>
<h2><u>Defined Values</u></h2>
<table id=arubaWiredVsfMIB width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMIB">arubaWiredVsfMIB</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>This MIB module describes objects used to manage Virtual
                   Switching Framework (VSF) feature.</ObjectDescription></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>MODULE-IDENTITY</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfObjects width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfObjects">arubaWiredVsfObjects</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT IDENTIFIER</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfConfig width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfConfig">arubaWiredVsfConfig</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.1</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT IDENTIFIER</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfStatus width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfStatus">arubaWiredVsfStatus</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.2</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT IDENTIFIER</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfNotifications width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfNotifications">arubaWiredVsfNotifications</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.1</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT IDENTIFIER</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfTrapEnable width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfTrapEnable">arubaWiredVsfTrapEnable</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.1.1</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>If set to 'true', SNMP traps will be generated for VSF events.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-write</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#TruthValue">TruthValue</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfOobmMADEnable width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfOobmMADEnable">arubaWiredVsfOobmMADEnable</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.1.2</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>Split detection scheme configured on the VSF stack. Supported
             schemes:
             'none`: No split detection. In the event of a stack split,
                     multiple fragments can be active.
             `mgmt`: The management network interface will be used to detect a
                     stack split. If multiple fragments are detected, only
                     the stack fragment containing the 'primary' member will
                     keep its network interfaces active.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-write</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>INTEGER</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>none(1), mgmt(2)</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfOperStatus width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfOperStatus">arubaWiredVsfOperStatus</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.2.1</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>Describes current split state of VSF stack. Split state can be
             one of the following:
             noSplit:          Both primary and secondary members are
                               physically present and operational.
             fragmemtActive:   A stack split has been detected and all network
                               interfaces in this fragment are active.
             fragmentInactive: A stack split has been detected and all network
                               interfaces in this fragment are inactive.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfTopology width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfTopology">arubaWiredVsfTopology</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.2.2</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>This object describes the physical topology of the VSF stack.
             Supported technologies include:
             standalone: The VSF stack comprises a single member only.
             chain:      The VSF stack members are connected in a daisy chain.
             ring:       The VSF stack members are connected in a ring.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberTable width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberTable">arubaWiredVsfMemberTable</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.3</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>This table contains information about the Virtual Switching
                 Framework members.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: not-accessible</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>SEQUENCE OF</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#ArubaWiredVsfMemberEntry">ArubaWiredVsfMemberEntry</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberEntry width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberEntry">arubaWiredVsfMemberEntry</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.3.1</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>A row in the Virtual Switching Framework member table.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: not-accessible</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#ArubaWiredVsfMemberEntry">ArubaWiredVsfMemberEntry</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberIndex width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberIndex">arubaWiredVsfMemberIndex</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.3.1.1</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>Virtual Switching Framework Member ID.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-SMI.php#Integer32">Integer32</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>1..65535</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberRole width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberRole">arubaWiredVsfMemberRole</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.3.1.2</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>Role of VSF member in stack.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberStatus width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberStatus">arubaWiredVsfMemberStatus</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.3.1.3</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>Specifies the status of the member-switch in the VSF
                 stack. The switch status can be one of:

                `notPresent`:            Member is not physically part of the
                                         stack.
                `booting`:               Member is booting up.
                `ready`:                 Member has finished booting, and its
                                         interfaces can forward traffic.
                `versionMismatch`:       Member is not running the same
                                         operating system version as the master
                                         switch.
                `communicationFailure`:  The master switch is unable to
                                         communicate with the member.
                `inOtherFragment`:       Member is part of another fragment as
                                         discovered through split detection.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberPartNumber width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberPartNumber">arubaWiredVsfMemberPartNumber</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.3.1.4</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>The Part Number Identifier of the VSF stack member.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberMacAddr width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberMacAddr">arubaWiredVsfMemberMacAddr</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.3.1.5</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>The switch base MAC address of this VSF stack member.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#MacAddress">MacAddress</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberProductName width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberProductName">arubaWiredVsfMemberProductName</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.3.1.6</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>This product name of this VSF stack member.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberSerialNum width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberSerialNum">arubaWiredVsfMemberSerialNum</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.3.1.7</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>The serial number identifier of this VSF stack member.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberBootImage width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberBootImage">arubaWiredVsfMemberBootImage</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.3.1.8</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>The software image version running on this VSF stack member.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberCpuUtil width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberCpuUtil">arubaWiredVsfMemberCpuUtil</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.3.1.9</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>The CPU utilization, in percentage, of this VSF stack member.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-SMI.php#Integer32">Integer32</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberMemoryUtil width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberMemoryUtil">arubaWiredVsfMemberMemoryUtil</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.3.1.10</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>The memory utilization, in percentage, of this VSF stack
                 member.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-SMI.php#Integer32">Integer32</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberBootTime width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberBootTime">arubaWiredVsfMemberBootTime</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.3.1.11</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>The boot up time, in seconds, of this VSF stack member.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-SMI.php#TimeTicks">TimeTicks</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberBootRomVersion width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberBootRomVersion">arubaWiredVsfMemberBootRomVersion</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.3.1.12</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>The software version of the running ServiceOS image on this
                 VSF stack member.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberTotalMemory width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberTotalMemory">arubaWiredVsfMemberTotalMemory</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.3.1.13</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>Specifies the total memory (RAM) available on this
                 VSF stack member.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-SMI.php#Integer32">Integer32</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>1..65535</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberCurrentUsage width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberCurrentUsage">arubaWiredVsfMemberCurrentUsage</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.3.1.14</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>Specifies the current memory (RAM) usage on this
                 VSF stack member.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-SMI.php#Integer32">Integer32</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>1..65535</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfLinkTable width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfLinkTable">arubaWiredVsfLinkTable</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.4</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>This table contains information about the Virtual Switching
                 Framework Links.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: not-accessible</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>SEQUENCE OF</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#ArubaWiredVsfLinkEntry">ArubaWiredVsfLinkEntry</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfLinkEntry width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfLinkEntry">arubaWiredVsfLinkEntry</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.4.1</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>A row in the Virtual Switching Framework Link table.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: not-accessible</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#ArubaWiredVsfLinkEntry">ArubaWiredVsfLinkEntry</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfLinkMemberId width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfLinkMemberId">arubaWiredVsfLinkMemberId</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.4.1.1</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>Virtual Switching Framework link member ID.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: not-accessible</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-SMI.php#Integer32">Integer32</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>1..65535</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfLinkId width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfLinkId">arubaWiredVsfLinkId</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.4.1.2</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>Virtual Switching Framework link ID.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: not-accessible</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-SMI.php#Integer32">Integer32</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>1..65535</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfLinkOperStatus width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfLinkOperStatus">arubaWiredVsfLinkOperStatus</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.4.1.3</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>The state of the VSF link.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-TC.php#DisplayString">DisplayString</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfLinkPeerMemberId width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfLinkPeerMemberId">arubaWiredVsfLinkPeerMemberId</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.4.1.4</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>The member ID of the peer switch on the link.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-SMI.php#Integer32">Integer32</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>1..65535</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfLinkPeerLinkId width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfLinkPeerLinkId">arubaWiredVsfLinkPeerLinkId</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.4.1.5</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>The link id of the peer member on the link.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/S/SNMPv2-SMI.php#Integer32">Integer32</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>1..65535</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfLinkPortList width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfLinkPortList">arubaWiredVsfLinkPortList</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.0.4.1.6</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>Interface(s) associated to the link.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType><a href="../../Html/Q/Q-BRIDGE-MIB.php#PortList">PortList</a></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberStatusChange width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberStatusChange">arubaWiredVsfMemberStatusChange</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.1.1</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>This notification is generated when a new member joins the VSF
            stack.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>NOTIFICATION-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfFragmentStatusChange width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfFragmentStatusChange">arubaWiredVsfFragmentStatusChange</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.1.2</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>This notification is generated when a stack fragment becomes
            active or inactive.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>NOTIFICATION-TYPE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfConformance width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfConformance">arubaWiredVsfConformance</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.2</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT IDENTIFIER</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfCompliances width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfCompliances">arubaWiredVsfCompliances</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.2.1</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT IDENTIFIER</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfGroups width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfGroups">arubaWiredVsfGroups</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.2.2</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT IDENTIFIER</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfConfigScalarGroup width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfConfigScalarGroup">arubaWiredVsfConfigScalarGroup</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.2.2.1</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>A collection of Virtual Switching Framework scalar objects.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-GROUP</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfStatusScalarGroup width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfStatusScalarGroup">arubaWiredVsfStatusScalarGroup</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.2.2.2</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>A collection of Virtual Switching Framework notifications
                 objects.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-GROUP</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMemberTableGroup width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMemberTableGroup">arubaWiredVsfMemberTableGroup</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.2.2.3</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>A collection of Virtual Switching Framework member table
                 objects.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-GROUP</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfLinkTableGroup width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfLinkTableGroup">arubaWiredVsfLinkTableGroup</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.2.2.4</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>A collection of Virtual Switching Framework link table
                 objects.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>OBJECT-GROUP</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfNotificationsGroup width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfNotificationsGroup">arubaWiredVsfNotificationsGroup</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.2.2.5</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>A collection of VSF virtual chassis notifications objects.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>NOTIFICATION-GROUP</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
<table id=arubaWiredVsfMibCompliance width="100%" border="1">
<tr>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectName><a href="../../Html/A/ARUBAWIRED-VSF-MIB.php#arubaWiredVsfMibCompliance">arubaWiredVsfMibCompliance</a></ObjectName></td>
<td width="25%" colspan="2" bgcolor="#c0c0c0"><ObjectOid>1.3.6.1.4.1.47196.4.1.1.3.10.2.1.1</ObjectOid></td>
</tr>
<tr>
<td width="25%" colspan="4" bgcolor="#ffffff"><ObjectDescription>The compliance statement for devices implementing the
                 ARUBA WIRED VSF Mib.</ObjectDescription></td>
</tr>
<tr>
<td width="50%" colspan="1" bgcolor="#ffffff"><ObjectStatus>Status: current</ObjectStatus></td>
<td width="50%" colspan="3" bgcolor="#ffffff"><ObjectAccess>Access: read-only</ObjectAccess></td>
</tr>
<tr>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>MODULE-COMPLIANCE</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType></ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
<td width="25%" colspan="1" bgcolor="#ffffff"><ObjectType>&nbsp;</ObjectType></td>
</tr>
</table>
<br>
</div>
<div id="body_footer">
Generation date: July 18, 2022, 13:41:17, <a href="http://www.circitor.fr">Copyright &copy; 2007 - 2022 - Circitor</a>
</div>
</div>
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
