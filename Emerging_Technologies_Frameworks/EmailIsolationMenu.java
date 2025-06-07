
// Email Isolation is one of the technology listed in FY21 vision (Mr. Stevel Wallace all hands on Oct 22, 2020).
// Email Isolation FRAMEWORK WAS DEVELOPED BASED ON several white papers and NIST Standards documents On Email security & Standards.
// The framework code was written by Randy Singh Computer Scientist,Technology Innovation Team (DISA/EM3) using programming in Java JGRASP (October, 2020)
// Randy Singh's Contact Phone# (301)225-9535  

import java.util.Scanner; 

public class EmailIsolationMenu

{

   public static void main(String[] args) 
   
   {
   
   // Declare a variable to hold the 
   // user's menu selection. 
   
      int menuSelection;
   
      final int MAX_VALUE = 17;
   
   // Declare variables to hold the units 
   // of measurement.
   
   //String DataTraffic, NumberOfConnections, InternetOfThings, IncreasedEnergyEfficiency, IncreasedOperationalExpenditures, NewUsecases, NewApplications,ApplicationDataSegmentation, AdminAuthenticationAuthorization, SecurityPolicyOrchestration,IdentityRequirements, HealthComplianceRequirements,
   //AuthorizationRequirements, AccountingAuditingRequirements, SegmentationRequirements, OrchestrationRequirements, AdditionalCloudDataTaggingDiscoveryRequirements, OptionalRequirements, Effectiveness, Suitability, Performance;
   
   // Create a Scanner object for keyboard input. 
   
      Scanner keyboard = new Scanner(System.in); 
   
   // Display the LIST OF EMAIL-ISOLATION MAIN MENU Categories 
   
      System.out.println();
      System.out.println   ("************************************************************************************************" );
      System.out.println();
      System.out.println   ("WELCOME TO EMAIL-ISOLATION FRAMEWORK APPLICATION.  ");
      System.out.println();
      System.out.println   ("HERE ARE EMAIL-ISOLATION-FRAMEWORK APPLICATION MAIN MENU: ");
      System.out.println();
      System.out.println   ("1.  EMAIL ISOLATION ELEMENTS. "); 
      System.out.println(); 
      System.out.println   ("2.  EMAIL STANDARDS ."); 
      System.out.println();
      System.out.println   ("3.  EMAIL SECURITY THREATS."); 
      System.out.println();
      System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
      System.out.println();
      System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
      System.out.println();
      System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
      System.out.println();
      System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
      System.out.println();
      System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
      System.out.println();
      System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
      System.out.println();
      System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
      System.out.println();
      System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
      System.out.println();
      System.out.println   ("12. SECURING EMAIL CLIENTS."); 
      System.out.println();
      System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
      System.out.println();
      System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
      System.out.println();
      System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
      System.out.println();
      System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
      System.out.println();
      System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
      System.out.println();
      System.out.println   ("************************************************************************************************" );
      System.out.println();
   
      System.out.print("PLEASE ENTER EMAIL-ISOLATION FRAMEWORK MAIN MENU CHOICES (1 - 17): ");
   
   
      menuSelection = keyboard.nextInt();
   
   // Validate the EMAIL-ISOLATION Menu selection. 
   
      while (menuSelection < 1 || menuSelection > 17) 
      
      {
      
         System.out.println("************************************************************************************************" );
         System.out.println(); 
         System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println("HERE ARE VALID EMAIL-ISOLATION-FRAMEWORK CATEGORIES LIST: ");
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
         System.out.println();
         System.out.println   ("2.  EMAIL STANDARDS ."); 
         System.out.println();
         System.out.println   ("3.  EMAIL SECURITY THREATS."); 
         System.out.println();
         System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
         System.out.println();
         System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
         System.out.println();
         System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
         System.out.println();
         System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
         System.out.println();
         System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
         System.out.println();
         System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
         System.out.println();
         System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
         System.out.println();
         System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
         System.out.println();
         System.out.println   ("12. SECURING EMAIL CLIENTS."); 
         System.out.println();
         System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
         System.out.println();
         System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
         System.out.println();
         System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
         System.out.println();
         System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
         System.out.println();
         System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
         System.out.println();
         System.out.println("************************************************************************************************" );
         System.out.println();
         System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CHOICE (1 - 17) FROM THE LIST ABOVE: ");
      
      
         menuSelection = keyboard.nextInt();
      
      } 
   
      while (menuSelection > 0 || menuSelection <= 17)
      
      
         switch(menuSelection)
         
         { 
         
         
            case 1:
            
               int menuSelect;
            
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("YOU SELECTED EMAIL-ELEMENTS CATEGORY OF EMAIL-ISOLATION FRAMEWORK ");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("PLEASE SEE BELOW EMAIL-ELEMENTS SUBCATEGORIES");
               System.out.println();
               System.out.println("************************************************************************************************" );
            
               EmailIsolationSetter Elements;
            
               Elements = new EmailIsolationSetter();
            
               System.out.println();  
               System.out.println("1.  EMAIL COMPONENTS.");
               System.out.println();
               System.out.println("2.  RELATED COMPONENTS.");
               System.out.println();
               System.out.println("3.  EMAIL PROTOCOLS.");
               System.out.println();
               System.out.println("4.  EMAIL FORMATS.");
               System.out.println();
               System.out.println("5.  SECURE WEB-MAIL SOLUTIONS.");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print(" ENTER YOUR EMAIL-ISOLATION FUNCTIONAL REQUIREMENTS CHOICE FROM (1 to 5) : ");
            
               menuSelect = keyboard.nextInt();
            
            
            
               while (menuSelect < 1 || menuSelect > 5)
               
               {
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println(); 
                  System.out.println("THIS IS INVALID CHOICE. ENTER YOUR VALID EMAIL-ELEMENTS CHOICE FROM 1 to 5:");
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("1.  EMAIL COMPONENTS.");
                  System.out.println();
                  System.out.println("2.  RELATED COMPONENTS.");
                  System.out.println();
                  System.out.println("3.  EMAIL PROTOCOLS.");
                  System.out.println();
                  System.out.println("4.  EMAIL FORMATS.");
                  System.out.println();
                  System.out.println("5.  SECURE WEB-MAIL SOLUTIONS.");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print(" ENTER YOUR EMAIL-ELEMENTS CHOICE FROM (1 to 5) : ");
               
               
                  menuSelect = keyboard.nextInt();
               
               }
            
               if ( menuSelect == 1)
               
               {          
                  System.out.println();
                  System.out.println("EMAIL-COMPONENTS: ");
                  System.out.println();
               
               
                  Elements.setComponents       ("Mail User Agents (MUAs):\r\nA MUA is a software component (or web interface) that allows an end user to compose and send messages and to one or more recipients.\r\nA MUA transmits new messages to a server for further processing (either final delivery or transfer to another server).\r\nThe MUA is also the component used by end users to access a mailbox where in-bound emails have been delivered.\r\nMUAs are available for a variety of systems including mobile hosts.\r\nThe proper secure configuration for an MUA depends on the MUA in question and the system it is running on.\r\nMUAs may utilize several protocols to connect to and communicate with email servers.\r\nThere may also be other features as well such as a cryptographic interface for producing encrypted and/or digitally signed email.\r\n\r\nMail Transfer Agents (MTAs):\r\nEmail is transmitted, in a “store and forward” fashion, across networks via Mail Transfer Agents(MTAs).\r\nMTAs communicate using the Simple Mail Transfer Protocol (SMTP) described below and act as both client and server, depending on the situation.\r\nFor example, an MTA can act as a server when accepting an email message from an end user's MUA, then act as a client in connecting to and transferring the message to the recipient domain's MTA for final delivery.\r\nMTAs can be described with more specialized language that denotes specific functions:\r\n\r\nMail Submission Agents (MSA):\r\nAn MTA that accepts mail from MUAs and begins the transmission process by sending it to a MTA for further processing.\r\nOften the MSA and first-hop MTA is the same process, just fulfilling both roles.\r\n\r\nMail Delivery Agent (MDA):\r\nAn MTA that receives mail from an organization's inbound MTA and ultimately places the message in a specific mailbox.\r\nLike the MSA,the MDA could be a combined in-bound MTA and MDA component.\r\nMail servers may also perform various security functions to prevent malicious email from being delivered or include authentication credentials such as digital signatures.\r\nThese security functions may be provided by other components that act as lightweight MTAs or these functions may be added to MTAs via filters or patches.\r\n\r\nAn email message may pass through multiple MTAs before reaching the final recipient.\r\nEach MTA in the chain may have its own security policy (which may be uniform within an organization,\r\nbut may not be uniform) and there is currently no way for a sender to request a particular level of security for the email message.\r\n\r\nSpecial Use Components:\r\nIn addition to MUAs and MTAs, an organization may use one or more special purpose components for a particular task.\r\nThese components may provide a security function such as malware filtering, or may provide some business process functionality such as email archiving or content filtering.\r\nThese components may exchange messages with other parts of the email infrastructure using all or part of the Simple Mail Transfer Protocol or use another protocol altogether.\r\nGiven the variety of components, there is no one single set of configurations for an administrator to deploy, and different organizations have deployed very different email architectures.\r\nAn administrator should consult the documentation for their given component and their existing sitespecific architecture.\r\n\r\nSpecial Considerations for Cloud and Hosted Service Customers:\r\nOrganizations that outsource their email service (whole or in part) may not have direct access to MTAs or any possible special use components.\r\nIn cases of Email as a Service (EaaS), the serviceprovider is responsible for the email infrastructure. Customers of Infrastructure as a Service (IaaS) may have sufficient access privileges to configure their email servers themselves.\r\nIn either architecture, the enterprise may have complete configuration control over MUAs in use.");        
               
               
                  System.out.println               ("" + Elements.getComponents());
                  System.out.println();          
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println( "TO CONTINUE WITH NEXT EMAIL-ELEMENTS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU  CHOICE # 1");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
               
               }
               
               else
               
                  if ( menuSelect == 2)
                  
                  {
                     System.out.println();
                     System.out.println();
                     System.out.println("EMAIL-RELATED-COMPONENTS:");
                     System.out.println();
                  
                     Elements.setERC ("\r\nIn addition to MUAs and MTAs, there are other network components used to support the email service for an organization.\r\nMost obviously is the physical infrastructure: the cables, wireless access points, routers and switches that make up the network.\r\nIn addition, there are network components used by email components in the process of completing their tasks.\r\nThis includes the Domain Name System, Public Key Infrastructure, and network security components that are used by the organization\r\n\r\nDomain Name System:\r\nThe Domain Name System (DNS) is a global, distributed database and associated lookup protocol.\r\nDNS is used to map a piece of information (most commonly a domain name) to an IP address used by a computer system.\r\nThe DNS is used by MUAs to find MSAs and MTAs to find the IP address of the next-hop server for mail delivery.\r\nSending MTAs query DNS for the Mail Exchange Resource Record (MX RR) of the recipient's domain (the part of an email address to the right of the “@” symbol) in order to find the receiving MTA to contact.\r\nIn addition to the “forward” DNS (translate domain names to IP addresses or other data), there is also the “reverse” DNS tree that is used to map IP addresses to their corresponding DNS name,or other data.\r\nTraditionally, the reverse tree is used to obtain the domain name for a given client based on the source IP address of the connection, but it is also used as a crude, highly imperfect authentication check.\r\nA host compares the forward and reverse DNS trees to check that the remote connection is likely valid and not a potential attacker abusing a valid IP address block.\r\nThis can be more problematic in IPv6, where even small networks can be assigned very large address blocks. Email anti-abuse consortiums recommend that enterprises should make sure that DNS reverse trees identify the authoritative mail servers for a domain [M3AAWG].\r\n\r\nThe DNS is also used as the publication method for protocols designed to protect email and combat malicious, spoofed email.\r\nTechnologies such as Sender Policy Framework (SPF),DomainKeys Identified Mail (DKIM) and other use the DNS to publish policy artifacts or public.\r\nkeys that can be used by receiving MTAs to validate that a given message originated from the purported sending domain's mail servers.\r\nIn addition,there are new proposals to encode end-user certificates (for S/MIME or OpenPGP) in the DNS using a mailbox as the hostname.\r\n\r\nA third use of the DNS with email is with reputation services.\r\nThese services provide information about the authenticity of an email based on the purported sending domain or originating IP address.\r\nThese services do not rely on the anti-spoofing techniques described above but through historical monitoring, domain registration history, and other information sources.\r\nThese services are often used to combat unsolicited bulk email (i.e. spam) and malicious email that could contain malware or links to subverted websites.\r\n\r\nThe Domain Name System Security Extensions (DNSSEC) provides cryptographic security for DNS queries.\r\nWithout security, DNS can be subjected to a variety of spoofing and man-in-the-middle attacks.\r\n\r\nEnterprise Perimeter Security Components:\r\nOrganizations may utilize security components that do not directly handle email, but may perform operations that affect email transactions.\r\nThese include network components like firewalls, Intrusion Detection Systems (IDS) and similar malware scanners.\r\nThese systems may not play any direct role in the sending and delivering of email but may have a significant impact if misconfigured.\r\nThis could result in legitimate SMTP connections being denied and the failure of valid email to be delivered.\r\nNetwork administrators should take the presence of these systems into consideration when making changes to an organization's email infrastructure.\r\nThis document makes no specific recommendations regarding these peripheral components.\r\n\r\nPublic Key Infrastructure (PKIX):\r\nOrganizations that send and receive S/MIME or OpenPGP protected messages, as well as those that use TLS, will also need to rely on the certificate infrastructure used with these protocols.\r\nThe certificate infrastructure does not always require the deployment of a dedicated system, but does require administrator time to obtain, configure and distribute security credentials to endusers.\r\nX.509 certificates can be used to authenticate one (or both) ends of a TLS connection when SMTP runs over TLS (usually MUA to MTA). S/MIME also uses X.509 certificates to certify and store public keys used to validate digital signatures and encrypt email.\r\nThe Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile is commonly called PKIX and is specified by.\r\nCertificate Authorities (CA) (or theorganization itself) issues X.509 certificates for an individual end-user or enterprise/business role (performed by a person or not) that sends email (for S/MIME). ");
                  
                  
                  
                     System.out.println("RELATED COMPONENTS: " + Elements.getERC());
                     System.out.println();
                     System.out.println("************************************************************************************************" );
                     System.out.println();
                     System.out.println( "TO CONTINUE WITH NEXT EMAIL-ISOLATION FUNCTIONAL CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                     System.out.println();
                     System.out.println("************************************************************************************************" );   
                  
                  }
                  
                  else
                  
                     if ( menuSelect == 3 )
                     
                     {
                        System.out.println();
                        System.out.println();
                        System.out.println("EMAIL-PROTOCOLS :");
                        System.out.println();  
                     
                        Elements.setProtocols("\r\nThere are two types of protocols used in the transmission of email. The first are the protocols used to transfer messages between MTAs and their end users (using MUAs).\r\nThe second is the protocol used to transfer messages between mail servers.\r\n\r\nSimple Mail Transfer Protocol (SMTP):\r\nEmail messages are transferred from one mail server to another (or from an MUA to MSA/MTA) using the Simple Mail Transfer Protocol (SMTP).\r\nSMTP was originally specified in 1982 in and has undergone several revisions, the most current being.\r\nSMTP is a text-based client-server protocol where the client (email sender) contacts the server (next-hop MTA) and issues a set of commands to tell the server about the message to be sent,and then transmits the message itself. The majority of these commands are ASCII text messages sent by the client and a resulting return code (also ASCII text) returned by the server.\r\n\r\nMail Access Protocols (POP3, IMAP, MAPI/RPC):\r\nMUAs typically do not use SMTP when retrieving mail from an end-user's mailbox.\r\nMUAs use another client-server protocol to retrieve the mail from a server for display on an end-user's host system. These protocols are commonly called Mail Access Protocols and are either Post Office Protocol (POP3) or Internet Message Access Protocol (IMAP). Most modern MUAs support both protocols but an enterprise service may restrict the use of one in favor of a single protocol for ease of administration or other reasons.\r\nPOP version 3 (POP3) is the simpler of the two protocols and typically downloads all mail for a user from the server, then deletes the copy on the server, although there is an option to maintain it on the server.\r\n1POP3 is similar to SMTP, in that the client connects to a port (normally port 110 or port 995 when using TLS) and sends ASCII commands\r\nto which the server are normally done in the clear, but an extension is available to do POP3 over TLS using the STLS command, which is very similar to the STARTTLS option in SMTP. Clients may connect initially over port 110 and invoke the STLS command, or alternatively, most servers allow TLS by default connections on port 995.\r\n\r\nIMAP is an alternative to POP3 but includes more built-in features that make it more appealing for enterprise use.\r\nIMAP clients can download email messages, but the messages remain on the server.\r\nThis and the fact that multiple clients can access the same mailbox simultaneously mean that end-users with multiple devices (laptop and smartphone for example),can keep their email synchronized across multiple devices. Like POP3, IMAP also has the ability to secure the connection between a client and a server.\r\nTraditionally, IMAP uses port 143 with no encryption.\r\nEncrypted IMAP runs over port 993, although modern IMAP servers also support the STARTTLS option on port 143.\r\n\r\nIn addition to POP3 and IMAP, there are other proprietary protocols in use with certain enterprise email implementations. Microsoft Exchange clients2 can use the Messaging Application Programming Interface (MAPI/RPC) to access a mailbox on a Microsoft Exchange server (and some other compatible implementations).\r\nSome cloud providers require clients to access their cloud-based mailbox using a web portal as the MUA instead of a dedicated email client.\r\nWith the exception of Microsoft’s Outlook Web Access, most web portals use IMAP to access the user’s mailbox.\r\n\r\nInternet Email Addresses Two distinct email addresses are used when sending an email via SMTP:\r\nthe SMTP MAIL FROM address and the email header FROM address.\r\nThe SMTP envelope MAIL FROM (also sometimes referred to as the RFC5321.From, or the return-path address, or envelope From:) isnfrom address used in the client SMTP.\r\nBoth types of contemporary email addresses consist of a local-part separated from a domain-part (a fully-qualified domain name) by an at-sign (e.g., local-part@domain-part).\r\n");
                     
                        System.out.println("ABSTRACTION OF FUNCTIONS FOR EMAIL-PROTOCOLS:" + Elements.getProtocols());    
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                        System.out.println();
                        System.out.println( "TO CONTINUE WITH NEXT EMAIL-ISOLATION FUNCTIONAL CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                     
                     }
                     
                     else
                     
                        if ( menuSelect == 4)
                        
                        {
                           System.out.println();
                           System.out.println("EMAIL-FORMATS: ");
                           System.out.println();
                        
                           Elements.setFormats("\r\nEmail messages may be formatted as plain text or as compound documents containing one or more components and attachments.\r\nModern email systems layer security mechanisms on top of these underlying systems.\r\n\r\nEmail Message Format:\r\nMulti-Purpose Internet Mail Extensions (MIME)Internet email was originally sent as plain text ASCII messages.\r\nThe Multi-purpose Internet Mail Extensions (MIME) allows email to containnon-ASCII character sets as well as other non-text message components and attachments.\r\nEssentially MIME allows for an email message to be broken into parts, with each part identified by a content type.\r\nTypical content types include text/plain (for ASCII text), image/jpeg, text/html, etc. A mail message may contain multiple parts, which themselves may contain multiple parts, allowing MIME-formatted messages to be included as attachments in other MIME-formatted messages.\r\nThe available types are listed in an IANA registry4 for developers, but not all may be understood by all MUAs.\r\n\r\nSecurity in MIME Messages (S/MIME):\r\nThe Secure Multi-purpose Internet Mail Extensions (S/MIME) is a set of widely implemented proposed Internet standards for cryptographically securing email.\r\nS/MIME provides authentication, integrity and non-repudiation (via digital signatures) and confidentiality (via encryption).\r\nS/MIME utilizes asymmetric keys for cryptography (i.e. public key cryptography) where the public portion is normally encoded and presented as X.509 digital certificates.\r\nWith S/MIME, signing digital signatures and message encryption are two distinct operations: messages can be digitally signed, encrypted, or both digitally signed and encrypted Because the process is first to sign and then encrypt, S/MIME is vulnerable to re-encryption attacks5; a protection is to include the name of the intended recipient in the encrypted message.\r\n\r\nPretty Good Privacy (PGP/OpenPGP):\r\nOpenPGP is an alternative proposed Internet standard for digitally signing and encrypting email.\r\nOpenPGP is an adaption of the message format implemented by the Pretty Good Privacy (PGP) email encryption system that was first released in 1991. Whereas the PGP formats were never formally specified, OpenPGP specifies open, royalty-free formatsfor encryption keys, signatures, and messages.\r\nToday the most widely used implementation of OpenPGP is Gnu Privacy Guard (gpg), an open source command-line program that runs on many platforms, with APIs in popular languages such as C, Python and Perl.\r\nMost desktop and web-based applications that allow users to send and receive OpenPGP-encrypted mail rely on gpg as the actual cryptographic engine.\r\n\r\nOpenPGP provides similar functionality as S/MIME, with three significant differences:\r\n\r\nKey Certification:\r\nWhereas X.509 certificates are issued by Certificate Authorities (or local agencies that have been delegated authority by a CA to issue certificates), users generate their own OpenPGP public and private keys and then solicit signatures for their public keys from individuals or organizations to which they are known.\r\nWhereas X.509 certificates can be signed by a single party, OpenPGP public keys can be signed by any number of parties.\r\nWhereas X.509 certificates are trusted if there is a valid PKIX chain to a trusted root, an OpenPGP public key is trusted if it is signed by another OpenPGP public key that is trusted by the recipient.\r\nThis is called the “Web-of-Trust.\r\n\r\nKey Distribution:\r\nOpenPGP does not always include the sender’s public key with each message, so it may be necessary for recipients of OpenPGP-messages to separately obtain the sender’s public key in order to verify the message or respond to the sender with an encrypted message. Many organizations post OpenPGP keys on SSL-protected websites;people who wish to verify digital signatures or send these organizations encrypted mail need to manually download these keys and add them to their OpenPGP clients.\r\nEssentially this approach exploits the X.509 certificate infrastructure to certify OpenPGP keys, albeit with a process that requires manual downloading and verification.\r\n\r\nKey Distribution:\r\nOpenPGP does not always include the sender’s public key with each message, so it may be necessary for recipients of OpenPGP-messages to separately obtain the sender’s public key in order to verify the message or respond to the sender with an encrypted message.\r\nMany organizations post OpenPGP keys on SSL-protected websites;people who wish to verify digital signatures or send these organizations encrypted mail need to manually download these keys and add them to their OpenPGP clients.\r\nEssentially this approach exploits the X.509 certificate infrastructure to certify OpenPGP keys, albeit with a process that requires manual downloading and verification.\r\n\r\nKey and Certificate Revocation:\r\nS/MIME keys are revoked using the PKIX revocation infrastructure of Certificate Revocation Lists and the Online Certificate Status Protocol (OCSP).\r\nThese protocols allow a certificate to be revoked at any time by the CA. With OpenPGP, in contrast a key is only allowed to be revoked by the key holder, and only with a Key Revocation Certificate. Thus, an OpenPGP user who loses access to a private key has no way to revoke the key if a Key Revocation Certificate was not prepared in advance.\r\nIf a Key Revocation Certificate does exist, the certificate can be uploaded to a PGP Key Server, OpenPGP key servers are generally not checked by a client that already has a copy of an OpenPGP key.\r\nThus, is it not clear how relying parties learn that an OpenPGP key has been revoked.\r\n\r\nThe Web-of-Trust is designed to minimize the problems of the key server. After an OpenPGP user downloads all of the keys associated with a particular email address, the correct OpenPGP certificate is selected by the signatures that it carries.\r\nBecause Web-of-Trust supports arbitrary validation geometries, it allows both the top-down certification geometry of X.509 as well as peer-to-peer approaches.\r\nHowever, studies have demonstrated that users find this process confusing, and the Web-of-Trust has not seen widespread adoption.\r\n\r\nLike S/MIME, among the biggest hurdles of deploying OpenPGP are the need for users to create certificates in advance, the difficulty of obtaining the certificate of another user in order to send an encrypted message, and incorporating this seamlessly into mail clients.\r\nHowever, in OpenPGP this difficulty impacts both digital signatures and encryption, since OpenPGP messages may not include the sender’s certificate.\r\n ");
                        
                           System.out.println("EMAIL-FORMATS: " + Elements.getFormats());      
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                           System.out.println();
                           System.out.println( "TO CONTINUE WITH NEXT EMAIL-ISOLATION FUNCTIONAL CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                        
                        }
                        
                        else
                        
                           if ( menuSelect == 5)
                           
                           {
                              System.out.println();         
                              System.out.println();
                              System.out.println("SECURE-WEB-MAIL-SOLUTIONS: "); 
                              System.out.println();     
                           
                           
                              Elements.setSWM("\r\nWhereas S/MIME and OpenPGP provide a security overlay for traditional Internet email, some organizations have adopted secure web-mail systems as an alternative approach for sending encrypted e-mail messages between users.\r\nSecure web-mail systems can protect email messagessolely with host-based security, or they can implement a cryptographic layer using S/MIME, OpenPGP, or other algorithms, such as the Boneh-Franklin (BF) and Boneh-Boyen (BB1) Identity-Based Encryption (IBE) algorithms.\r\n\r\nSecure webmail systems can perform message decryption at the web server or on the end-users client. In general, these systems are less secure than end-to-end systems because the private key is under the control of the web server, which also has access to the encrypted message.\r\nThese systems cannot guarantee non-repudiation, since the server has direct access to the signing key.\r\n\r\nAn exception is webmail-based systems that employ client-side software to make use of a private key stored at the client—for example, a webmail plug-in that allows the web browser to make use of a private key stored in a FIPS-201 compliant smartcard.\r\nIn these cases, the message is decrypted and displayed at the client, and the server does not access the decrypted text of the message.");
                           
                           
                              System.out.println("SECURE-WEB-MAIL-SOLUTIONS:" + Elements.getSWM());
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                              System.out.println();
                              System.out.println( "TO CONTINUE WITH NEXT EMAIL-ISOLATION FUNCTIONAL CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                           
                           }
                           
                           
                           else
                           
                              System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println   ("HERE ARE EMAIL-ISOLATION FRAMEWORK MAIN MAENU CATEGORIES LIST: ");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println   ("1.  EMAIL ISOLATION ELEMENTS. "); 
               System.out.println();
               System.out.println   ("2.  EMAIL STANDARDS ."); 
               System.out.println();
               System.out.println   ("3.  EMAIL SECURITY THREATS."); 
               System.out.println();
               System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
               System.out.println();
               System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
               System.out.println();
               System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
               System.out.println();
               System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
               System.out.println();
               System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
               System.out.println();
               System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
               System.out.println();
               System.out.println   ("12. SECURING EMAIL CLIENTS."); 
               System.out.println();
               System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
               System.out.println();
               System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
               System.out.println();
               System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
            
               menuSelection = keyboard.nextInt();
            
               while (menuSelection < 1 || menuSelection > 17) 
               
               {
               
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();  
                  System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("HERE IS THE VALID LIST OF EMAIL-ISOLATION MAIN MENU CATEGORIES: ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println   ("1.  EMAIL ISOLATION ELEMENTS. "); 
                  System.out.println();
                  System.out.println   ("2.  EMAIL STANDARDS ."); 
                  System.out.println();
                  System.out.println   ("3.  EMAIL SECURITY THREATS."); 
                  System.out.println();
                  System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
                  System.out.println();
                  System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
                  System.out.println();
                  System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
                  System.out.println();
                  System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
                  System.out.println();
                  System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
                  System.out.println();
                  System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
                  System.out.println();
                  System.out.println   ("12. SECURING EMAIL CLIENTS."); 
                  System.out.println();
                  System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
                  System.out.println();
                  System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
                  System.out.println();
                  System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 18) FROM THE LIST ABOVE: ");
               
               
               
                  menuSelection = keyboard.nextInt();
               
               
               } 
            
               break;
         
         
            case 2: 
            
               EmailIsolationSetter Standards;
            
               Standards = new EmailIsolationSetter();
            
               System.out.println();
            
               System.out.println("YOU SELECTED EMAIL-STANDARDS CATEGORY FROM EMAIL-ISOLATION MAIN MENU ");
               System.out.println();
               System.out.println("PLEASE SEE BELOW EMAIL-STANDARDS SUBCATEGORIES");
               System.out.println();
               System.out.println("1.   BACKGROUND & MESSAGE FLOW .");
               System.out.println();
               System.out.println("2.   MULTIPURPOSE INTERNET MAIL EXTENSIONS .");
               System.out.println();
               System.out.println("3.   MAIL TRANSPORT STANDARDS.");
               System.out.println();
               System.out.println("4.   SIMPLE MAIL TRANSFER PROTOCOL.");
               System.out.println();
               System.out.println("5.   SIMPLE MAIL TRANSFER PROTOCOL EXTENSIONS.");
               System.out.println();
               System.out.println("6.   PROPRIETARY MAIL TRANSPORTS .");
               System.out.println();
               System.out.println("7.   CLIENT ACCESS STANDARDS.");
               System.out.println();
               System.out.println("8.   POST OFFICE PROTOCOL.");
               System.out.println();
               System.out.println("9.   INTERNET MESSAGE ACCESS PROTOCOL.");
               System.out.println();
               System.out.println("10.  PROPRIETARY MAIL BOX ACCESS MECHANISM.");
               System.out.println();
               System.out.println("11.  WEB-BASED MAIL ACCESS.");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print(" ENTER YOUR CHOICE FROM EMAIL-STANDARDS (1 to 11) : ");
            
            
               menuSelect = keyboard.nextInt();
            
               while (menuSelect < 1 || menuSelect > 11)
               
               
               
               {
                  System.out.println("************************************************************************************************" );
               
                  System.out.println("THIS IS INVALID EMAIL-STANDARDS SUBCATEGORY SELECTION"); 
                  System.out.println();
                  System.out.println("PLEASE SELECT A VALID CHOICE FROM THE LIST BELOW"); 
                  System.out.println();
                  System.out.println("1.   BACKGROUND & MESSAGE FLOW .");
                  System.out.println();
                  System.out.println("2.   MULTIPURPOSE INTERNET MAIL EXTENSIONS .");
                  System.out.println();
                  System.out.println("3.   MAIL TRANSPORT STANDARDS.");
                  System.out.println();
                  System.out.println("4.   SIMPLE MAIL TRANSFER PROTOCOL.");
                  System.out.println();
                  System.out.println("5.   SIMPLE MAIL TRANSFER PROTOCOL EXTENSIONS.");
                  System.out.println();
                  System.out.println("6.   PROPRIETARY MAIL TRANSPORTS .");
                  System.out.println();
                  System.out.println("7.   CLIENT ACCESS STANDARDS.");
                  System.out.println();
                  System.out.println("8.   POST OFFICE PROTOCOL.");
                  System.out.println();
                  System.out.println("9.   INTERNET MESSAGE ACCESS PROTOCOL.");
                  System.out.println();
                  System.out.println("10.  PROPRIETARY MAIL BOX ACCESS MECHANISM.");
                  System.out.println();
                  System.out.println("11.  WEB-BASED MAIL ACCESS.");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print(" ENTER YOUR CHOICE FROM EMAIL-STANDARDS (1 to 11) : ");
               
               
                  menuSelect = keyboard.nextInt();
               
               
               }
            
            
            
               if ( menuSelect == 1)
               
               {          
                  System.out.println();
                  System.out.println("EMAIL-STANDARDS SUBCATEGORIES: ");
                  System.out.println();
               
               
                  Standards.setBMF  ("\r\nThe process starts with message composition. The most basic mail clients typically ask the user to\r\nprovide the following: subject line, message content, and intended recipients. When these fields are\r\ncompleted and the user sends the message, the message is transformed into a specific standard format \r\nspecified by Request for Comments (RFC) 2822, Internet Message Format. At the most basic level, the \r\ntwo primary message sections are the header and the body. The header section contains the vital \r\ninformation about the message including origination date, sender, recipient(s), delivery path, subject, and \r\nformat information. The body of the message contains the actual content of the message.\r\n\r\nOnce the message is translated into an RFC 2822 formatted message, it can be transmitted. Using a \r\nnetwork connection, the mail client, referred to as a mail user agent (MUA), connects to a mail transfer \r\nagent (MTA) operating on the mail server. After initiating communication, the mail client provides \r\nthe sender’s identity to the server. Next, using the mail server commands, the client tells the server who the \r\nintended recipients are. Although the message contains a list of intended recipients, the mail server does \r\nnot examine the message for this information. Only after the complete recipient list is sent to the server \r\ndoes the client supply the message. From this point, message delivery is under control of the mail server.\r\n\r\nOnce the mail server is processing the message, several events occur: recipient server identification, \r\nconnection establishment, and message transmission. Using Domain Name System (DNS) services, the sender’s mail server determines the mail server(s) for the recipient(s). Then, the server opens up a connection(s) to the recipient mail server(s) and sends the message employing a process similar to that used by the originating client. At this point, one of two events could occur. If the sender’s and recipient’s mailboxes are located on the same mail server, the message is delivered using a local delivery agent (LDA). If the sender’s and recipient’s mailboxes are located on different mail servers, the send process is repeated from one MTA to another until the message reaches the recipient’s mailbox.\r\n\r\n. ");
               
               
                  System.out.println    ("BACKGROUND & MESSAGE FLOW = " + Standards.getBMF());
                  System.out.println();          
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println( "TO CONTINUE WITH NEXT EMAIL-STANDARDS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU  CHOICE # 2");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
               
               }
               
               else
               
                  if ( menuSelect == 2)
                  
                  {
                     System.out.println();
                     System.out.println();
                     System.out.println("MULTIPURPOSE-INTERNE-MAIL-EXTENSIONS-SUBCATEGORY: ");
                     System.out.println();
                  
                     Standards.setMIME ("RFC 2822 provides a standard for transmitting messages containing textual content; however, it does not address messages that contain attachments, such as a mail message with a word processing document or photo included. Making use of the headers in an RFC 2822 message, the Multipurpose Internet Mail Extensions (MIME) provide almost endless possibilities to describe the structure of rich message content.\r\nMIME uses the convention of content-type/subtype pairs to specify the native representation or encoding of associated data. Examples of content types include the following:\r\n\r\nAudio – for transmitting audio or voice data.\r\nApplication – used to transmit application data or binary data.\r\n\r\nImage – for transmitting still image (picture) data.\r\n\r\nMessage – for encapsulating another mail message.\r\n\r\nMultipart – used to combine several message body parts, possibly of differing types of data, into a single message.\r\n\r\nText – used to represent textual information in a number of character sets and formatted text description languages in a standardized manner.\r\n\r\nVideo – for transmitting video or moving image data, possibly with audio as part of the composite video data format.\r\n\r\nThe current MIME standards include five parts: RFCs 2045, 2046, 2047, 4289 (which replaced 2048), and 2049 (see Appendix B).\r\nThey address message body format, media types, non-American Standard Code for Information Interchange (non-ASCII) message header extensions, registration procedures, and conformance criteria, respectively. With this added functionality, email features such as message attachments and inline hypertext markup language (HTML) are possible. Although MIME extensions allow for binary message content, such content is incorporated into an RFC 2822 message using Base64 encoding, which provides a textual representation of binary data. ");
                  
                  
                  
                     System.out.println("MULTIPURPOSE INTERNET MAIL EXTENSIONS = " + Standards.getMIME());
                     System.out.println();
                     System.out.println("************************************************************************************************" );
                     System.out.println();
                     System.out.println( "TO CONTINUE WITH NEXT EMAIL-STANDARDS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 2");
                     System.out.println();
                     System.out.println("************************************************************************************************" );   
                  
                  }
                  
                  else
                  
                     if ( menuSelect == 3 )
                     
                     {
                        System.out.println();
                        System.out.println();
                        System.out.println("PLEASE SEE BELOW ABSTRACTION OF FUNCTIONS FOR MAIL-TRANSPORT-STANDARDS: ");
                        System.out.println();  
                     
                        Standards.setMTS("To ensure reliability and interoperability among various mail applications, mail transport standards were established. In the simplest scenario, an email message is sent from one local user to another local user. For this case, an LDA is responsible for placing the message in the appropriate mailbox. When a message is sent to non-local recipients, an MTA is needed to send the message from the local mail server to the remote mail server. Depending on the type of systems involved, different MTAs may be used, which in turn may support different implementations of a particular message transfer protocol or more than one distinct transfer protocol.\r\n\r\nThe most common MTA transfer protocol is the Simple Mail Transfer Protocol (SMTP). SMTP is the de-facto Internet standard for sending email messages. Thus, any Internet messaging system must support SMTP to facilitate communication with other email messaging applications. Other messaging systems exist that use different MTA transfer protocols between similar or clustered messaging systems. ");
                     
                        System.out.println(" MAIL-TRANSPORT-STANDARDS = " + Standards.getMTS());    
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                        System.out.println();
                        System.out.println( "TO CONTINUE WITH NEXT EMAIL-STANDARDS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 2");
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                     
                     }
                     
                     else
                     
                        if ( menuSelect == 4)
                        
                        {
                           System.out.println();
                           System.out.println("PLEASE SEE BELOW SIMPLE-MAIL-TRANSFER-PROTOCOL: ");
                           System.out.println();
                        
                           Standards.setSMT("Jon Postel of the University of Southern California developed SMTP in August 1982. As RFC 821, Simple Mail Transfer Protocol, states, “SMTP was developed to ensure a more reliable and efficient way to transport messages.\r\nAt the most basic level, SMTP is a minimal language that defines a communications protocol for delivering email messages.\r\n\r\nWhen a user sends an email, the client contacts its SMTP server and conducts a “conversation” using the SMTP language.\r\n A MUA is typically part of the mail client application (e.g., Outlook, Eudora).\r\nIf an MUA is unavailable, email messages can be sent using a Telnet client connected to the SMTP service. Figure 2.3 depicts a sample SMTP conversation using Telnet.\r\nThe Telnet and SMTP commands entered by the user for this session are shown in bold. During a manual SMTP Telnet session, the HELP command can be used to determine which of the SMTP commands are enabled on the server. ");
                        
                           System.out.println(" SIMPLE-MAIL-TRANSFER-PROTOCOL= " + Standards.getSMT());      
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                           System.out.println();
                           System.out.println( "TO CONTINUE WITH NEXT EMAIL-STANDARDS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 2");
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                        
                        }
                        
                        else
                        
                           if ( menuSelect == 5)
                           
                           {
                              System.out.println();         
                              System.out.println();
                              System.out.println("SIMPLE-MAIL-TRANSFER-PROTOCOL-EXTENSIONS: "); 
                              System.out.println();     
                           
                           
                              Standards.setSMTE("As the number of email users grew, additional functionality was sought in mail clients and SMTP servers.\r\nFor SMTP servers to support this additional functionality, extensions were added to SMTP.\r\nIn 1993, RFC 1425 introduced the concept of SMTP service extensions.\r\nSubsequently, RFC 1425 was superseded by RFC 1651 in 1994, RFC 1869 in 1995, and RFC 2821 in 2001.\r\nThese RFCs added three pieces to the SMTP framework:\r\nNew SMTP commands Registry for SMTP service extensions (RFC 1651) Additional parameters for SMTP MAIL FROM and RCPT TO commands (RFC 1869).\r\nTo be compatible with older SMTP servers, there needed to be a method to allow the mail client application to determine whether the server supported extensions.\r\nThis was accomplished through the “enhanced hello” (EHLO) command. When connecting to a server, a mail client could issue the EHLO command.\r\nIf the server supported SMTP extensions, it would give a successful response and list the extensions that were supported.\r\nIf the server did not support SMTP extensions, it would issue a command failure response prompting the MUA to respond with the standard HELO command.\r\nServers that support SMTP extensions, also known as Extended SMTP (ESMTP), typically respond with ESMTP in their banner.\r\nNumerous extensions are supported by a variety of SMTP servers.\r\nIn particular, RFC 2554 specifies a new command and protocol for identifying and authenticating a user.\r\nThe default configuration of most mail servers typically does not have authenticated relay enabled.");  
                           
                              System.out.println("" + Standards.getSMTE());
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                              System.out.println();
                              System.out.println( "TO CONTINUE WITH NEXT EMAIL-STANDARDS FUNCTIONAL CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 2");
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                           
                           }
                           
                           else
                           
                              if ( menuSelect == 6)
                              
                              {
                                 System.out.println();
                                 System.out.println();
                                 System.out.println("PROPRIETARY-MAIL-TRANSPORTS: ");
                                 System.out.println();
                              
                              
                                 Standards.setPMT("As mentioned previously, some messaging systems use MTAs that do not support either SMTP or ESMTP.\r\nThese types of MTAs are designed to work within a closed messaging environment.\r\nMany large-scale government, academic, and private organizations have messaging systems that use these types of MTAs.\r\nHowever, these organizations still rely on SMTP or ESMTP-capable MTAs for communicating with external messaging systems.\r\nSome examples of messaging systems that use proprietary protocols are MTAs for Lotus Notes and Microsoft Exchange.\r\nDiscussion on the benefits and disadvantages of using MTAs that support only proprietary message transfer protocols is outside the scope of this document. ");        
                              
                                 System.out.println("" + Standards.getPMT());
                                 System.out.println();
                                 System.out.println("************************************************************************************************" );
                                 System.out.println();
                                 System.out.println( "TO CONTINUE WITH NEXT EMAIL-ISOLATION FUNCTIONAL CATEGORY PLEASE SELECT AGAINEMAIL-ISOLATION MAIN MENU CHOICE # 2");
                                 System.out.println();
                                 System.out.println("************************************************************************************************" );        
                              
                              }
                              
                              else
                              
                                 if ( menuSelect == 7)
                                 
                                 {
                                    System.out.println();
                                    System.out.println();
                                    System.out.println("CLIENT-ACCESS-STANDARDS: ");
                                    System.out.println();
                                    Standards.setCAS("Once a message is delivered by the LDA, users need to access the mail server to retrieve the message.\r\nMail clients (MUAs) are used to access the mail server and retrieve email messages.\r\nSeveral methods exist for users to access their mailboxes, the simplest being direct access.\r\nThe simplest scenario for a messaging system would be one in which all users have direct access to their mailbox (common on hosts employing the Unix operating system).\r\nFor each account that exists on the system, there is a corresponding mailbox in that user’s home directory. When messages are received, users can use command line-based mail programs, such as mail or pine, to directly access the mailbox.\r\nAlthough this method is straightforward, it requires all users accessing the mail server to receive messages to have a user account and a command-line interface on the host operating system.\r\nAllowing users, particularly external users, to have access to a command-line interface is a significant security risk.\r\nTo mitigate this risk, mailbox access protocols were devised.\r\nThe two most widely supported mailbox access protocols are Post Office Protocol (POP) and Internet Message Access Protocol (IMAP).\r\nAs with message transfer protocols for MTAs, other proprietary mailbox access protocols exist that are regularly used by commercial software manufacturers,.\r\nIt is important to understand that POP, IMAP, and indeed most proprietary protocols in their default configuration use cleartext.passwords for authentication, which can be intercepted by other hosts attached to the network.");
                                 
                                    System.out.println("" + Standards.getCAS());
                                    System.out.println();
                                    System.out.println("************************************************************************************************" );
                                    System.out.println();
                                    System.out.println( "TO CONTINUE WITH NEXT EMAIL-ISOLATION CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 2");
                                    System.out.println();
                                    System.out.println("************************************************************************************************" );
                                 
                                 
                                 }
                                 else
                                 
                                    if ( menuSelect == 8)
                                    
                                    {
                                       System.out.println();
                                       System.out.println();
                                       System.out.println("PLEASE SEE BELOW POST-OFFICE-PROTOCOL: ");
                                       System.out.println();
                                    
                                       Standards.setPOP("POP was first developed in 1984. At its core, POP was nothing more than a way to copy messages from the mail server mailbox to the mail client.\r\nIt worked much like a traditional post office mailbox.\r\nThe mail client opens a connection to the mail server mailbox, downloads the email messages, and then closes the connection.\r\nSince 1984, POP has gone through several changes and is now in its third iteration as defined in RFC 1939.\r\nThe basic command set is very similar to the command set of 1984; however, POP version 3 offers a few new optional commands.\r\nFrom a security standpoint, the addition of the APOP was important, since it avoids transmitting a user’s password in the clear.\r\nInstead, a challenge/response mechanism is used, by which the client responds with a cryptographic hash of the combined challenge sent from the server and the user's password, for verification by a POP mail server performing the same operation for the user in question.\r\nPOP3 Extension Mechanism, defines an extension to POP3 that allows clients to discover additional information about POP3 servers, such as which extensions and optional commands they support.\r\nThe POP mailbox access standard has some significant limitations.\r\nTypically, when users retrieve their email, copies of the messages that reside on the server are deleted. This means that the user has the sole responsibility of maintaining message archives.\r\nAlthough this may be acceptable for personal accounts, it is generally unacceptable for most commercial or governmental organizations that have to meet certain legal requirements.\r\nIn addition, if a user employs several workstations for retrieving email, the messages are dispersed on multiple hosts. POP may be configured so that the original messages are not deleted from the server.\r\nHowever, the user will either have to download all of the messages previously viewed as well as the new messages when accessing a mailbox from another host, or have to set up a retention period after which messages are automatically deleted from the server.");
                                    
                                       System.out.println("" + Standards.getPOP());
                                       System.out.println();
                                       System.out.println("************************************************************************************************" );
                                       System.out.println();
                                       System.out.println( "TO CONTINUE WITH NEXT EMAIL-ISOLATION CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 2");
                                       System.out.println();
                                       System.out.println("************************************************************************************************" );
                                    
                                    
                                    } 
                                    
                                    else
                                    
                                       if ( menuSelect == 9)
                                       
                                       {
                                          System.out.println();
                                          System.out.println();
                                          System.out.println("INTERNET-MESSAGE-ACCESS-PROTOCOL: ");
                                          System.out.println();
                                       
                                       
                                          Standards.setIMAP("To address the above-mentioned issues with POP, IMAP was developed in 1988.\r\nThe IMAP protocol was developed as a functional superset of the POP version 2 protocol.\r\nAt the most basic level, IMAP was designed so user mailboxes could be centrally located and accessed from multiple mail clients or MUAs.\r\nInitially, IMAP offered very little functionality beyond that of POP, but since 1988, it has evolved into a robust mailbox access protocol.\r\nThe current edition of the IMAP standard is RFC 3501: Internet Message Access Protocol – Because IMAP supports many different features, it has a much wider command set than that of POP.\r\nIMAP has been extended with a challenge/response mechanism comparable to APOP, which is called the Challenge-Response Authentication Mechanism (CRAM).\r\nCRAM requires the client to make note of the challenge data sent by the server and respond with a string consisting of the user’s name, a space, and a digest computed by applying a keyed hash algorithm6 against the timestamp sent with the challenge, using a shared secret as the key. ");        
                                       
                                          System.out.println("" + Standards.getIMAP());
                                          System.out.println();
                                          System.out.println("************************************************************************************************" );
                                          System.out.println();
                                          System.out.println( "TO CONTINUE WITH NEXT EMAIL-ISOLATION CATEGORY PLEASE SELECT AGAINEMAIL-ISOLATION MAIN MENU CHOICE # 2");
                                          System.out.println();
                                          System.out.println("************************************************************************************************" );        
                                       
                                       }
                                       
                                       else
                                       
                                          if ( menuSelect == 10)
                                          
                                          {
                                             System.out.println();
                                             System.out.println();
                                             System.out.println("PLEASE SEE BELOW PROPRIETARY-MAIL-BOX-ACCESS-MECHANISM:");
                                             System.out.println();
                                             Standards.setPMAM("Proprietary mailbox access protocols are designed to work within closed messaging environments.\r\nMicrosoft Exchange and Lotus Notes are examples of messaging systems that use proprietary mailbox access protocols.\r\nThese proprietary protocols offer additional functionality when used with their associated clients.\r\nNearly all proprietary messaging systems support standard protocols, including SMTP, POP, and IMAP, in order to interoperate with other types of MTAs and MUAs.\r\nOrganizations must decide for themselves whether it is appropriate to support proprietary protocols in their mail clients and servers.\r\nAs mentioned earlier, regardless of whether they are standard or proprietary, most access protocols default to weak authentication mechanisms (unencrypted authentication information).\r\nTherefore, organizations need to configure the access protocols to support stronger forms of authentication. ");
                                          
                                             System.out.println(" " + Standards.getPMAM());
                                             System.out.println();
                                             System.out.println("************************************************************************************************" );
                                             System.out.println();
                                             System.out.println( "TO CONTINUE WITH NEXT EMAIL-ISOLATION CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 2");
                                             System.out.println();
                                             System.out.println("************************************************************************************************" );
                                          
                                          
                                          }
                                          else
                                          
                                             if ( menuSelect == 11)
                                             
                                             {
                                                System.out.println();
                                                System.out.println();
                                                System.out.println("WEB-BASED-MAIL-ACCESS:");
                                                System.out.println();
                                             
                                                Standards.setWMA("Web-based mail applications, also known as Webmail applications, are increasingly being used as a means of email service delivery,\r\nbecause Web browsers that enable access to the client are available on nearly every Internet-enabled device. A user simply runs a Web browser and connects to a Web site that hosts the Web-based mail application.\r\nThe connection is made using either Hypertext Transfer Protocol (HTTP) or HTTP over Transport Layer Security (TLS), also known as HTTPS. HTTPS encrypts the communications, which protects both authentication information and email message content.\r\nHTTP alone does not offer any protection, so organizations should consider using HTTPS for Web-based mail application communications.\r\nWeb-based mail applications incorporate much of the mail-handling functionality of traditional mail clients and communicate with their associated mail servers using the same mailbox access protocols described earlier—SMTP, POP, and IMAP, as well as proprietary protocols.\r\nThe mailbox access protocols are used between the Web servers and mail servers only; the protocols are not carried between the Web servers and Web browsers");
                                             
                                             
                                                System.out.println(" " + Standards.getWMA());
                                                System.out.println();
                                                System.out.println("************************************************************************************************" );
                                                System.out.println();
                                                System.out.println( "TO CONTINUE WITH NEXT EMAIL-ISOLATION FUNCTIONAL CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 2");
                                                System.out.println();
                                                System.out.println("************************************************************************************************" );
                                             
                                             
                                             } 
                                             
                                             
                                             else 
                                             
                                                System.out.println();
               System.out.println   ("HERE ARE EMAIL-ISOLATION FRAMEWORK MAIN MENU CATEGORIES LIST: ");
               System.out.println();
               System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
               System.out.println();
               System.out.println   ("2.  EMAIL STANDARDS ."); 
               System.out.println();
               System.out.println   ("3.  EMAIL SECURITY THREATS."); 
               System.out.println();
               System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
               System.out.println();
               System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
               System.out.println();
               System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
               System.out.println();
               System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
               System.out.println();
               System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
               System.out.println();
               System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
               System.out.println();
               System.out.println   ("12. SECURING EMAIL CLIENTS."); 
               System.out.println();
               System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
               System.out.println();
               System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
               System.out.println();
               System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
            
               menuSelection = keyboard.nextInt();
            
               while (menuSelection < 1 || menuSelection > 17) 
               
               {
               
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();  
                  System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("HERE IS THE VALID LIST OF EMAIL-ISOLATION MAIN MENU CATEGORIES: ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
                  System.out.println();
                  System.out.println   ("2.  EMAIL STANDARDS ."); 
                  System.out.println();
                  System.out.println   ("3.  EMAIL SECURITY THREATS."); 
                  System.out.println();
                  System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
                  System.out.println();
                  System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
                  System.out.println();
                  System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
                  System.out.println();
                  System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
                  System.out.println();
                  System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
                  System.out.println();
                  System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
                  System.out.println();
                  System.out.println   ("12. SECURING EMAIL CLIENTS."); 
                  System.out.println();
                  System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
                  System.out.println();
                  System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
                  System.out.println();
                  System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 18) FROM THE LIST ABOVE: ");
               
               
               
                  menuSelection = keyboard.nextInt();
               
               
               } 
            
            
               break; 
         
            case 3:
            
               EmailIsolationSetter  Threats;
               Threats = new EmailIsolationSetter();
            
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println("YOU SELECTED EMAIL-SECURITY-THREATS CATEGORY FROM EMAIL-ISOLATION MAIN MENU");
               System.out.println();
               System.out.println("PLEASE SEE BELOW EMAIL-SECURITY-THREATS SUBCATEGORIES:");
               System.out.println();
               System.out.println("1.   INTEGRITY RELATED THREATS.");
               System.out.println(); 
               System.out.println("2.   CONFIDENTIALITY RELATED THREATS");
               System.out.println();
               System.out.println("3.   AVAILABILITY RELATED THREATS.");
               System.out.println();
               System.out.println("4.   UNAUTHORIZED EMAIL SENDERS WITHIN ORGANIZATIONS IP ADDRESS BLOCK.");
               System.out.println();
               System.out.println("5.   UNAUTHORIZED EMAIL RECEIVER WITHIN ORGANIZATIONS IP ADDRESS BLOCK.");
               System.out.println();
               System.out.println("6.   UNAUTHORIZED EMAIL MESSAGES FROM A VALID DNS DOMAIN (ADDRESS SPOOFING).");
               System.out.println();
               System.out.println("7.   TEMPERING/MODIFICATION OF EMAIL CONTENT.");
               System.out.println();
               System.out.println("8.   DNS CACHE POISONING.");
               System.out.println();
               System.out.println("9.   PHISHING AND SPEAR PHISHING.");
               System.out.println();
               System.out.println("10.  EMAIL BOMBING.");
               System.out.println();
               System.out.println("11.  UNSOLICITED BULK EMAIL (SPAM).");
               System.out.println();
               System.out.println("12.  AVAILABILITY OF EMAIL SERVERS.");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print(" ENTER YOUR EMAIL-THREAT CHOICE FROM (1 to 12): ");
            
            
               menuSelect = keyboard.nextInt();
            
            
               while (menuSelect < 1 || menuSelect > 12)
               
               
               {
                  System.out.println();
                  System.out.println("************************************************************************************************" );  
                  System.out.println    ("THIS IS INVALID SELECTION"); 
                  System.out.println();
                  System.out.println(     "PLEASE SEE BELOW VALID LIST OF EMAIL-SECURITY-THREATS");
                  System.out.println();
                  System.out.println("1.   INTEGRITY RELATED THREATS.");
                  System.out.println(); 
                  System.out.println("2.   CONFIDENTIALITY RELATED THREATS");
                  System.out.println();
                  System.out.println("3.   AVAILABILITY RELATED THREATS.");
                  System.out.println();
                  System.out.println("4.   UNAUTHORIZED EMAIL SENDERS WITHIN ORGANIZATIONS IP ADDRESS BLOCK.");
                  System.out.println();
                  System.out.println("5.   UNAUTHORIZED EMAIL RECEIVER WITHIN ORGANIZATIONS IP ADDRESS BLOCK.");
                  System.out.println();
                  System.out.println("6.   UNAUTHORIZED EMAIL MESSAGES FROM A VALID DNS DOMAIN (ADDRESS SPOOFING).");
                  System.out.println();
                  System.out.println("7.   TEMPERING/MODIFICATION OF EMAIL CONTENT.");
                  System.out.println();
                  System.out.println("8.   DNS CACHE POISONING.");
                  System.out.println();
                  System.out.println("9.   PHISHING AND SPEAR PHISHING.");
                  System.out.println();
                  System.out.println("10.  EMAIL BOMBING.");
                  System.out.println();
                  System.out.println("11.  UNSOLICITED BULK EMAIL (SPAM).");
                  System.out.println();
                  System.out.println("12.  AVAILABILITY OF EMAIL SERVERS.");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print(" ENTER YOUR EMAIL-THREAT CHOICE FROM (1 to 12): ");
               
               
               
               
                  menuSelect = keyboard.nextInt();
               
               
               }
            
            // If-else Type ocode starts here****************
            
               if ( menuSelect == 1)
               
               {          
                  System.out.println();
                  System.out.println("INTEGRITY-THREATS : ");
                  System.out.println();
               
               
                  Threats.setIR           ("Integrity-related threats to the email system, which could result in unauthorized access\r\nto an enterprises’ email system, or spoofed email used to initiate an attack.\r\nIntegrity in the context of an email service assumes multiple dimensions. Each dimension can be\r\nthe source of one or more integrity-related threats:\r\n\r\n• Unauthorized email senders within an organization’s IP address block\r\n\r\n• Unauthorized email receivers within an organization’s IP address block\r\n\r\n• Unauthorized email messages from a valid DNS domain\r\n\r\n• Tampering/Modification of email content from a valid DNS domain\r\n\r\n• DNS Cache Poisoning\r\n\r\n• Phishing and spear phishing");
               
               
                  System.out.println               ("" +  Threats.getIR());
                  System.out.println();          
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println( "TO CONTINUE WITH NEXT EMAIL-THREATS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU  CHOICE # 3");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
               
               }
               
               else
               
                  if ( menuSelect == 2)
                  
                  {
                     System.out.println();
                     System.out.println();
                     System.out.println("CONFIDENTIALITY-THREATS: ");
                     System.out.println();
                  
                     Threats.setCRT ("Confidentiality-related threats to email, which could result in unauthorized disclosure\r\nof sensitive information.\r\n\r\nA confidentiality-related threat occurs when the data stream containing email messages with\r\nsensitive information are accessible to an adversary. The type of attack that underlies this threat\r\ncan be passive since the adversary has only requires read access but not write access to the email\r\ndata being transmitted. There are two variations of this type of attack include:\r\n\r\n- The adversary may have access to the packets that make up the email message as they move\r\nover a network. This access may come in the form of a passive wiretapping or eavesdropping attack.\r\n\r\n- Software may be installed on a MTA that makes copies of email messages and delivers them\r\nto the adversary. For example, the adversary may have modified the target’s email account so\r\nthat a copy of every received message is forwarded to an email address outside the organization.\r\n\r\nEncryption is the best defense against eavesdropping attacks. Encrypting the email messages\r\neither between MTAs can thwart attacks involving packet\r\ninterception. End-to-end encryption can protect against both\r\neavesdropping attacks as well as MTA software compromise.\r\n\r\nA second form of passive attack is a traffic analysis attack. In this scenario, the adversary is not\r\nable to directly interpret the contents of an email message, mostly due to the fact that the\r\nmessage is encrypted. However, since inference of information is still possible in certain\r\ncircumstances (depending upon interaction or transaction context) from the observation of\r\nexternal traffic characteristics (volume and frequency of traffic between any two entities) and\r\nhence the occurrence of this type of attack constitutes a confidentiality threat.\r\n\r\nAlthough the impact of traffic analysis is limited in scope, it is much easier to perform this attack\r\nin practice—especially if part of the email transmission media uses a wireless network, if packets\r\nare sent over a shared network, or if the adversary has the ability to run network management or\r\nmonitoring tools against the victim’s network. TLS encryption provides some protection against\r\ntraffic analysis attacks, as the attacker is prevented from seeing any message headers. End-to-end\r\nemail encryption protocols do not protect message headers, as the headers are needed for\r\ndelivery to the destination mailbox. Thus, organizations may wish to employ both kinds of\r\nencryption to secure email from confidentiality threats.");
                  
                  
                  
                     System.out.println("" +  Threats.getCRT());
                     System.out.println();
                     System.out.println("************************************************************************************************" );
                     System.out.println();
                     System.out.println( "TO CONTINUE WITH NEXT EMAIL-THREATS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 3");
                     System.out.println();
                     System.out.println("************************************************************************************************" );   
                  
                  }
                  
                  else
                  
                     if ( menuSelect == 3 )
                     
                     {
                        System.out.println();
                        System.out.println();
                        System.out.println("AVAILABILITY-THREATS ");
                        System.out.println();  
                     
                        Threats.setART("Availability-related threats to the email system, which could prevent end users from\r\nbeing able to send or receive email.\r\n\r\nAn availability threat exists in the email infrastructure (or for that matter any IT infrastructure),\r\nwhen potential events occur that prevents the resources of the infrastructure from functioning\r\naccording to their intended purpose. The following availability-related threats exist in an email infrastructure.\r\n\r\n• Email Bombing\r\n\r\n• Unsolicited Bulk Email (UBE) – also called “Spam”\r\n\r\n• Availability of email servers");
                     
                        System.out.println("" +  Threats.getART());    
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                        System.out.println();
                        System.out.println( "TO CONTINUE WITH NEXT EMAIL-THREATS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 3");
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                     
                     }
                     
                     else
                     
                        if ( menuSelect == 4)
                        
                        {
                           System.out.println();
                           System.out.println("UNAUTHORIZED-EMAIL-SENDERS-WITHIN-ORGANIZATIONS-IP-ADDRESS-BLOCK. ");
                           System.out.println();
                        
                           Threats.setUMS("An unauthorized email sender is some MSA or MTA that sends email messages that appear to be\r\nfrom a user in a specific domain (e.g. user@example.com), but is not identified as a legitimate\r\nmail sender by the organization that runs the domain.\r\n\r\nThe main risk that an unauthorized email sender may pose to an enterprise is that a sender may\r\nbe sending malicious email and using the enterprise’s IP address block and reputation to avoid\r\nanti-spam filters. A related risk is that the sender may be sending emails that present themselves\r\nas legitimate communications from the enterprise itself.\r\n\r\nThere are many scenarios that might result in an unauthorized email sender:\r\n\r\n• Malware present on an employee’s laptop may be sending out email without the employee’s knowledge.\r\n\r\n• An employee (or intruder) may configure and operate a mail server without authorization.\r\n\r\n• A device such as a photocopier or an embedded system may contain a mail sender that is\r\nsending mail without anyone’s knowledge.\r\n\r\nOne way to mitigate the risk of unauthorized senders is for the enterprise to block outbound port\r\n25 (used by SMTP) for all hosts except those authorized to send mail.\r\n\r\nSecurity Recommendation 1:\r\n\r\nTo mitigate the risk of unauthorized sender, an enterprise\r\nadministrator should block outbound port 25 (except for authorized mail senders) and look to\r\ndeploy firewall or intrusion detection systems (IDS) that can alert the administrator when an\r\nunauthorized host is sending mail via SMTP to the Internet.\r\n\r\nThe proliferation of virtualization greatly increases the risk that an unauthorized virtual server\r\nrunning on a virtual machines (VMs) within a particular enterprise might send email. This is\r\nbecause many VMs are configured by default to run email servers (MTAs), and many VM\r\nhypervisors use network address translation (NAT) to share a single IP address between multiple\r\nVMs. Thus, a VM that is unauthorized to send email may share an IP address with a legitimate\r\nemail sender. To prevent such a situation, ensure that VMs that are authorized mail senders and\r\nthose VMs that are not authorized, do not share the same set of outbound IP addresses. An easy\r\nway to do this is assigning these VMs to different NAT instances. Alternatively, internal firewall\r\nrules can be used to block outbound port 25 for VMs that are not authorized to send outbound email.\r\n\r\nSecurity Recommendation 2:\r\n\r\nSystems that are not involved in the organization’s email\r\ninfrastructure should be configured to not run Mail Transfer Agents (MTAs). Internal systems\r\nthat need to send mail should be configured to use a trusted internal MSA.");
                        
                           System.out.println("" + Threats.getUMS());      
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                           System.out.println();
                           System.out.println( "TO CONTINUE WITH NEXT EMAIL-THREATS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 3");
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                        
                        }
                        
                        else
                        
                           if ( menuSelect == 5)
                           
                           {
                              System.out.println();         
                              System.out.println();
                              System.out.println("UNAUTHORIZED-EMAIL-RECEIVER-WITHIN-ORGANIZATIONS-IP-ADDRESS-BLOCK. "); 
                              System.out.println();     
                           
                           
                              Threats.setUMR("Unauthorized mail receivers are a risk to the enterprise IT security posture because they may be\r\nan entry point for malicious email. If the enterprise email administrator does not know of the\r\nunauthorized email receiver, they cannot guarantee the server is secure and provides the\r\nappropriate mail handling rules for the enterprise such as scanning for malicious links/code,\r\nfiltering spam, etc. This could allow malware to bypass the enterprise perimeter defenses and\r\nenter the local network undetected.\r\n\r\nSecurity Recommendation:\r\n\r\nTo mitigate the risk of unauthorized receivers, an enterprise\r\nadministrator should block inbound port 25 and look to deploy firewall or intrusion detection\r\nsystems (IDS) that can alert the administrator when an unauthorized host is accepting mail via\r\nSMTP from the Internet.");
                           
                           
                              System.out.println("" + Threats.getUMR());
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                              System.out.println();
                              System.out.println( "TO CONTINUE WITH NEXT EMAIL-THREATS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 3");
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                           
                           }
                           
                           else
                           
                              if ( menuSelect == 6)
                              
                              {
                                 System.out.println();
                                 System.out.println();
                                 System.out.println("UNAUTHORIZED-EMAIL-MESSAGES-FROM-A-VALID-DNS-DOMAIN (ADDRESS SPOOFING). ");
                                 System.out.println();
                              
                              
                                 Threats.setUMAS("Just as organizations face the risk of unauthorized email senders, they also face the risk that they\r\nmight receive email from an unauthorized sender. This is sometimes called “spoofing,”\r\nespecially when one group or individual sends mail that appears to come from another. In a\r\nspoofing attack, the adversary spoofs messages using another (sometimes even non-existent)\r\nuser’s email address.");        
                              
                                 System.out.println("" + Threats.getUMAS());
                                 System.out.println();
                                 System.out.println("************************************************************************************************" );
                                 System.out.println();
                                 System.out.println( "TO CONTINUE WITH NEXT EMAIL-THREATS CATEGORY PLEASE SELECT AGAINEMAIL-ISOLATION MAIN MENU CHOICE # 3");
                                 System.out.println();
                                 System.out.println("************************************************************************************************" );        
                              
                              }
                              
                              else
                              
                                 if ( menuSelect == 7)
                                 
                                 {
                                    System.out.println();
                                    System.out.println();
                                    System.out.println("TEMPERING/MODIFICATION-OF-EMAIL-CONTENT. ");
                                    System.out.println();
                                    Threats.setTMD("The content of an email message, just like any other message content traveling over the Internet,\r\nis liable to be altered in transit. Hence the content of the received email may not be the same as\r\nwhat the sender originally composed. The countermeasure for this threat is for the sender to\r\ndigitally sign the message, attach the signature to the plaintext message and for the receiver to\r\nverify the signature.\r\n\r\nThere are several solutions available to mitigate this risk by either encrypting the transmission of\r\nemail messages between servers using Transport Layer Security (TLS) for SMTP or using an\r\nend-to-end solution to digitally sign email between initial sender and final receiver.");
                                 
                                    System.out.println("" + Threats.getTMD());
                                    System.out.println();
                                    System.out.println("************************************************************************************************" );
                                    System.out.println();
                                    System.out.println( "TO CONTINUE WITH NEXT EMAIL-THREATS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 3");
                                    System.out.println();
                                    System.out.println("************************************************************************************************" );
                                 
                                 
                                 }
                                 else
                                 
                                    if ( menuSelect == 8)
                                    
                                    {
                                       System.out.println();
                                       System.out.println();
                                       System.out.println("DNS-CACHE-POISONING-CATEGORY. ");
                                       System.out.println();
                                    
                                       Threats.setDCP("Email systems rely on DNS for many functions. Some of them are:\r\n\r\nThe sending MTA uses the DNS to find the IP address of the next-hop email server\r\n(assuming the To: address is not a local mailbox).\r\n\r\n• The recipient email server (if domain based email authentication is supported) uses the\r\nDNS to look for appropriate records in the sending DNS domain either to authenticate the\r\nsending email server (using SPF) or to authenticate an email message for its origin\r\ndomain (using DKIM).\r\n\r\nThere are risks to using the DNS as a publication mechanism for authenticating email. First,\r\nthose highly motivated to conduct phishing/spam campaigns, may attempt to spoof a given\r\ndomain’s DNS-based email authentication mechanisms in order to continue to deliver spoofed\r\nemail masquerading as the domain in question. The second risk is that an attacker would spoof a\r\ndomain’s DNS-based authentication mechanisms in order to disrupt legitimate email from the\r\nsource domain. For example, maliciously spoofing the SPF record of authorized mail relays, to\r\nexclude the domains legitimate MTAs, could result in all legitimate email from the target domain\r\nbeing dropped by other MTAs. Lastly, a resolver whose cache has been poisoned can potentially\r\nreturn the IP address desired by an attacker, rather than the legitimate IP address of a queried\r\ndomain name. In theory, this allows email messages to be redirected or intercepted.\r\n\r\nAnother impact of a DNS server with a poisoned cache as well as a compromised web server is\r\nthat the users are redirected to a malicious server/address when attempting to visit a legitimate\r\nweb site. If this phenomenon occurs due to a compromised web server, it is termed as pharming.\r\nAlthough the visit to a legitimate web site can occur by clicking on a link in a received email.\r\n\r\nAs far as DNS cache poisoning is concerned, DNSSEC security extension\r\ncan provide protection from these kind of attacks since it ensures the\r\nintegrity of DNS resolution through an authentication chain from the root to the target domain of\r\nthe original DNS query. However, even the presence of a single non-DNSSEC aware server in\r\nthe chain can compromise the integrity of the DNS resolution.");
                                    
                                       System.out.println("" + Threats.getDCP());
                                       System.out.println();
                                       System.out.println("************************************************************************************************" );
                                       System.out.println();
                                       System.out.println( "TO CONTINUE WITH NEXT EMAIL-THREATS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 3");
                                       System.out.println();
                                       System.out.println("************************************************************************************************" );
                                    
                                    
                                    } 
                                    
                                    else
                                    
                                       if ( menuSelect == 9)
                                       
                                       {
                                          System.out.println();
                                          System.out.println();
                                          System.out.println("PHISHING-AND-SPEAR-PHISHING-CATEGORY ");
                                          System.out.println();
                                       
                                       
                                          Threats.setPSP("Phishing is the process of illegal collection of private/sensitive information using a spoofed\r\nemail as the means. This is done with the intention of committing identity theft, gaining access to\r\ncredit cards and bank accounts of the victim etc. Adversaries use a variety of tactics to make the\r\nrecipient of the email into believing that they have received the phishing email from a legitimate\r\nuser or a legitimate domain, including:\r\n\r\n• Using a message-From: address that looks very close to one of the legitimate addresses\r\nthe user is familiar with or from someone claiming to be an authority (IT administrator,manager, etc.).\r\n\r\n• Using the email’s content to present to the recipient an alarm, a financial lure, or\r\notherwise attractive situation, that either makes the recipient panic or tempts the recipient\r\ninto taking an action or providing requested information.\r\n\r\n• Sending the email from an email using a legitimate account holder’s software or\r\ncredentials, typically using a bot that has taken control of the email client or malware that\r\nhas stolen the user’s credentials.\r\n\r\nAs part of the email message, the recipient may usually be asked to click on a link to what\r\nappears like a legitimate website, but in fact is a URL that will take the recipient into a spoofed\r\nwebsite set up by the adversary. If the recipient clicks on the embedded URL, the victim often\r\nfinds that the sign-in page, logos and graphics are identical to the legitimate website in the\r\nadversary-controlled website, thereby creating the trust necessary to make the recipient submit\r\nthe required information such as user ID and the password. Some attackers use web pages to\r\ndeliver malware directly to the victim’s web browser.\r\n\r\nIn many instances, the phishing emails are generated in thousands without focus on profile of the\r\nvictims. Hence they will have a generic greeting such as “Dear Member”, “Dear Customer” etc.\r\nA variant of phishing is spear phishing where the adversary is aware of, and specific about, the\r\nvictim’s profile. More than a generic phishing email, a spear phishing email makes use of more\r\ncontext information to make users believe that they are interacting with a legitimate source. For\r\nexample, a spear phishing email may appear to relate to some specific item of personal\r\nimportance or a relevant matter at the organization –for instance, discussing payroll\r\ndiscrepancies or a legal matter. As in phishing, the ultimate motive is the same – to lure the\r\nrecipient to an adversary-controlled website masquerading as a legitimate website to collect\r\nsensitive information about the victim or attack the victim’s computer.\r\n\r\nThere are two minor variations of phishing: clone phishing and whaling. Clone phishing is the\r\nprocess of cloning an email from a legitimate user carrying an attachment or link and then\r\nreplacing the link or attachment alone with a malicious version and then sending altered email\r\nfrom an email address spoofed to appear to come from the original sender (carrying the pretext of re-sending or sending an updated version).\r\n Whaling is a type of phishing specifically targeted\r\nagainst high profile targets so that the resulting damage carries more publicity and/or financial\r\nrewards for the perpetrator is more.\r\n\r\nThe most common countermeasures used against phishing are domain-based checks such as SPF,\r\nDKIM and DMARC (see Section 4). More elaborate is to design anti-phishing filters that can\r\ndetect text commonly used in phishing emails, recovering hidden text in images, intelligent word\r\nrecognition – detecting cursive, hand-written, rotated or distorted texts as well as the ability to\r\ndetect texts on colored backgrounds. While these techniques will not prevent malicious email\r\nsent using compromised legitimate accounts, they can be used to reduce malicious email sent\r\nfrom spoofed domains or spoofed “From:” addresses.");        
                                       
                                          System.out.println("" + Threats.getPSP());
                                          System.out.println();
                                          System.out.println("************************************************************************************************" );
                                          System.out.println();
                                          System.out.println( "TO CONTINUE WITH NEXT EMAIL-THREATS CATEGORY PLEASE SELECT AGAINEMAIL-ISOLATION MAIN MENU CHOICE # 3");
                                          System.out.println();
                                          System.out.println("************************************************************************************************" );        
                                       
                                       }
                                       
                                       else
                                       
                                          if ( menuSelect == 10)
                                          
                                          {
                                             System.out.println();
                                             System.out.println();
                                             System.out.println("EMAIL-BOMBING-CATEGORY. ");
                                             System.out.println();
                                             Threats.setEMB("Email bombing is a type of attack that involves sending several thousands of identical messages\r\nto a particular mailbox in order to cause overflow. These can be many large messages or a very\r\nlarge number of small messages. Such a mailbox will either become unusable for the legitimate\r\nemail account holder to access. No new messages can be delivered and the sender receives an\r\nerror asking to resend the message. In some instances, the mail server may also crash.\r\n\r\nThe motive for Email bombing is denial of service (DoS) attack. A DoS attack by definition\r\neither prevents authorized access to resources or causes delay (e.g., long response times) of timecritical\r\noperations. Hence email bombing is a major availability threat to an email system since it\r\ncan potentially consume substantial Internet bandwidth as well as storage space in the message\r\nstores of recipients. An email bombing attack can be launched in several ways.\r\n\r\nThere are many ways to perpetrate an email bombing attack, including:\r\n\r\n• An adversary can employ any (anonymous) email account to constantly bombard the victim’s\r\nemail account with arbitrary messages (that may contain very long large attachments).\r\n\r\n• If an adversary controls an MTA, the adversary can run a program that automatically\r\ncomposes and transmits messages.\r\n\r\n• An adversary can post a controversial or significant official statement to a large audience\r\n(e.g., a social network) using the victim’s return email address. Humans will read the\r\nmessage and respond with individually crafted messages that may be very hard to filter with\r\nautomated techniques. The responses to this posting will eventually flood the victim’s email account.\r\n\r\n• An adversary may subscribe the victim’s email address to many mailing lists (“listservers”).\r\nThe generated messages are then sent to the victim, until the victim’s email address is\r\nunsubscribed from those lists.\r\n\r\nPossible countermeasures for protection against Email bombing are: (a) Use filters that are based\r\non the logic of filtering identical messages that are received within a chosen short span of time\r\nand (b) configuring email receivers to block messages beyond a certain size and/or attachments\r\nthat exceed a certain size.");
                                          
                                             System.out.println("" + Threats.getEMB());
                                             System.out.println();
                                             System.out.println("************************************************************************************************" );
                                             System.out.println();
                                             System.out.println( "TO CONTINUE WITH NEXT EMAIL-THREATS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 3");
                                             System.out.println();
                                             System.out.println("************************************************************************************************" );
                                          
                                          
                                          }
                                          else
                                          
                                             if ( menuSelect == 11)
                                             
                                             {
                                                System.out.println();
                                                System.out.println();
                                                System.out.println("UNSOLICITED-BULK-EMAIL-(SPAM)-CATEGORY. ");
                                                System.out.println();
                                             
                                                Threats.setUBE("Spam is the internet slang for unsolicited bulk email (UBE). Spam refers to indiscriminately sent\r\nmessages that are unsolicited, unwanted, irrelevant and/or inappropriate, such as commercial\r\nadvertising in mass quantities. Thus spam, generally, is not targeted towards a particular email\r\nreceiver or domain. However, when the volume of spam coming into a particular email domain\r\nexceeds a certain threshold, it has availability implications since it results in increased network\r\ntraffic and storage space for message stores. Spam that looks for random gullible victims or\r\ntargets particular users or groups of users with malicious intent (gathering sensitive information\r\nfor physical harm or for committing financial fraud) is called phishing. From the above\r\ndiscussion of email bombing attacks, it should be clear that spam can sometimes be a type of\r\nemail bombing.\r\n\r\nProtecting the email infrastructure against spam is a challenging problem. This is due to the fact\r\nthat the two types of techniques currently used to combat spam have limitations.");
                                             
                                                System.out.println("" + Threats.getUBE());
                                                System.out.println();
                                                System.out.println("************************************************************************************************" );
                                                System.out.println();
                                                System.out.println( "TO CONTINUE WITH NEXT EMAIL-THREATS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 3");
                                                System.out.println();
                                                System.out.println("************************************************************************************************" );
                                             
                                             
                                             } 
                                             else
                                             
                                                if ( menuSelect == 12)
                                                
                                                {
                                                   System.out.println();
                                                   System.out.println();
                                                   System.out.println("AVAILABILITY-OF-EMAIL-SERVERS-CATEGORY. ");
                                                   System.out.println();
                                                
                                                   Threats.setAES("The email infrastructure just like any other IT infrastructure should provide for fault tolerance\r\nand avoid single points of failure. A domain with only a single email server or a domain with\r\nmultiple email servers, but all located in a single IP subnet is likely to encounter availability\r\nproblems either due to software glitches in MTA, hardware maintenance issues or local data\r\ncenter network problems. The typical measures for ensuring high availability of email as a\r\nservice are: (a) Multiple MTAs with placement based on the email traffic load encountered by\r\nthe enterprise; and, (b) Distribution of email servers in different network segments or even physical locations.");
                                                
                                                   System.out.println("" + Threats.getAES());
                                                   System.out.println();
                                                   System.out.println("************************************************************************************************" );
                                                   System.out.println();
                                                   System.out.println( "TO CONTINUE WITH NEXT EMAIL-THREATS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 3");
                                                   System.out.println();
                                                   System.out.println("************************************************************************************************" );
                                                
                                                
                                                } 
                                                
                                                
                                                else 
                                                
                                                
                                                
                                                   System.out.println();
               System.out.println   ("HERE ARE EMAIL-ISOLATION-FRAMEWORK MAIN MENU CATEGORIES LIST: ");
               System.out.println();
               System.out.println   ("1.  EMAIL ISOLATION ELEMENTS. "); 
               System.out.println();
               System.out.println   ("2.  EMAIL STANDARDS ."); 
               System.out.println();
               System.out.println   ("3.  EMAIL SECURITY THREATS."); 
               System.out.println();
               System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
               System.out.println();
               System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
               System.out.println();
               System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
               System.out.println();
               System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
               System.out.println();
               System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
               System.out.println();
               System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
               System.out.println();
               System.out.println   ("12. SECURING EMAIL CLIENTS."); 
               System.out.println();
               System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
               System.out.println();
               System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
               System.out.println();
               System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
            
               menuSelection = keyboard.nextInt();
            
               while (menuSelection < 1 || menuSelection > 17) 
               
               {
               
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();  
                  System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("HERE IS THE VALID LIST OF EMAIL-ISOLATION MAIN MENU CATEGORIES: ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
                  System.out.println();
                  System.out.println   ("2.  EMAIL STANDARDS ."); 
                  System.out.println();
                  System.out.println   ("3.  EMAIL SECURITY THREATS."); 
                  System.out.println();
                  System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
                  System.out.println();
                  System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
                  System.out.println();
                  System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
                  System.out.println();
                  System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
                  System.out.println();
                  System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
                  System.out.println();
                  System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
                  System.out.println();
                  System.out.println   ("12. SECURING EMAIL CLIENTS."); 
                  System.out.println();
                  System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
                  System.out.println();
                  System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
                  System.out.println();
                  System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 18) FROM THE LIST ABOVE: ");
               
               
                  menuSelection = keyboard.nextInt();
               
               } 
            
               break;
         
            case 4:
            
               EmailIsolationSetter  UC;
               UC = new EmailIsolationSetter();
            
            
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println("YOU SELECTED USE-CASES CATEGORY FROM EMAIL-ISOLATION MAIN MENU");
               System.out.println();
               System.out.println("PLEASE SEE BELOW IDENTIFIED USE-CASES CATEGORIES: ");
               System.out.println(); 
               System.out.println("1.  CONTROL DEVICE ACCESS TO EMAIL ATTACHMENTS.");
               System.out.println();
               System.out.println("2.  ENSURE CONFIDETIALITY OF SENSITIVE COMMUNICATIONS.");
               System.out.println();
               System.out.println("3.  IDENTIFY EXPLICIT IMAGES TO ENFORCE ACCEPTABLE USE.");
               System.out.println();
               System.out.println("4.  SPAM AND PHISHING PROTECTION.");
               System.out.println();
               System.out.println("5.  EDUCATE USERS TO SECURITY AWARENESS.");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER YOUR CHOICE FROM ARCHITECTURAL REQUIREMENTS CATEGORIES 1 to 5: ");
            
            
               menuSelect = keyboard.nextInt();
            
               while (menuSelect < 1 || menuSelect > 5)
               
               { 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println(); 
                  System.out.println("THIS IS INVALID SELECTION FOR USE-CASES CATEGORY"); 
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW VALID USE-CASES SELECTIONS:");
                  System.out.println();
                  System.out.println("1.  CONTROL DEVICE ACCESS TO EMAIL ATTACHMENTS.");
                  System.out.println();
                  System.out.println("2.  ENSURE CONFIDETIALITY OF SENSITIVE COMMUNICATIONS.");
                  System.out.println();
                  System.out.println("3.  IDENTIFY EXPLICIT IMAGES TO ENFORCE ACCEPTABLE USE.");
                  System.out.println();
                  System.out.println("4.  SPAM AND PHISHING PROTECTION.");
                  System.out.println();
                  System.out.println("5.  EDUCATE USERS TO SECURITY AWARENESS.");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER YOUR CHOICE FROM ARCHITECTURAL REQUIREMENTS CATEGORIES 1 to 5: ");
               
               
                  menuSelect = keyboard.nextInt();
               
               }
               if ( menuSelect == 1)
               
               {          
                  System.out.println();
                  System.out.println("CONTROL-DEVICE-ACCESS-TO-EMAIL-ATTACHMENTS: ");
                  System.out.println();
               
               
                  UC.setCDA           ("Prevent total access to sensitive email attachments on vulnerable unmanaged devices (BYOD)\r\nwhile permitting full access to secure managed devices.");
               
               
                  System.out.println      ("" +  UC.getCDA());
                  System.out.println();          
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println( "TO CONTINUE WITH NEXT EMAIL-USE-CASES CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU  CHOICE # 4");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
               
               }
               
               else
               
                  if ( menuSelect == 2)
                  
                  {
                     System.out.println();
                     System.out.println();
                     System.out.println("ENSURE-CONFIDETIALITY-OF-SENSITIVE-COMMUNICATIONS: ");
                     System.out.println();
                  
                     UC.setCSC ("Enable secure delivery of email communications with Forcepoint Email Encryption that\r\neliminates the traditional barriers of cost and complexity by offering easy administration,\r\nwithout key management or additional hardware.");
                  
                  
                  
                     System.out.println("" +  UC.getCSC());
                     System.out.println();
                     System.out.println("************************************************************************************************" );
                     System.out.println();
                     System.out.println( "TO CONTINUE WITH NEXT EMAIL-USE-CASES CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 4");
                     System.out.println();
                     System.out.println("************************************************************************************************" );   
                  
                  }
                  
                  else
                  
                     if ( menuSelect == 3 )
                     
                     {
                        System.out.println();
                        System.out.println();
                        System.out.println("TO-IDENTIFY-EXPLICIT-IMAGES-TO-ENFORCE-ACCEPTABLE-USE: ");
                        System.out.println();  
                     
                        UC.setIEI("The Forcepoint Image Analysis Module allows employers to proactively monitor,\r\neducate, and enforce company email policy for explicit or pornographic image attachments.");
                     
                        System.out.println("" +  UC.getIEI());    
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                        System.out.println();
                        System.out.println( "TO CONTINUE WITH NEXT EMAIL-USE-CASES CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 4");
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                     
                     }
                     
                     else
                     
                        if ( menuSelect == 4)
                        
                        {
                           System.out.println();
                           System.out.println("SPAM-AND-PHISHING-PROTECTION: ");
                           System.out.println();
                        
                           UC.setSAPP("Detect unwanted spam and unsafe phishing emails, allowing customers to block,\r\nquarantine, or take other actions.");
                        
                           System.out.println("" + UC.getSAPP());      
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                           System.out.println();
                           System.out.println( "TO CONTINUE WITH NEXT EMAIL-USE-CASES CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 4");
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                        
                        }
                        
                        else
                        
                           if ( menuSelect == 5)
                           
                           {
                              System.out.println();         
                              System.out.println();
                              System.out.println("EDUCATE-USERS-TO-SECURITY-AWARENESS: "); 
                              System.out.println();     
                           
                           
                              UC.setESA("Unique phishing education with feedback capabilities educates employees as they\r\nmake mistakes, helping them to better learn and understand safe email best practices.");
                           
                           
                              System.out.println("" + UC.getESA());
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                              System.out.println();
                              System.out.println( "TO CONTINUE WITH NEXT EMAIL-USE-CASES CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 4");
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                           
                           }
                           
                           else
                           
                              System.out.println();
               System.out.println   ("HERE ARE EMAIL-ISOLATION-FRAMEWORK MAIN MENU CATEGORIES LIST: ");
               System.out.println();
               System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
               System.out.println();
               System.out.println   ("2.  EMAIL STANDARDS ."); 
               System.out.println();
               System.out.println   ("3.  EMAIL SECURITY THREATS."); 
               System.out.println();
               System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
               System.out.println();
               System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
               System.out.println();
               System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
               System.out.println();
               System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
               System.out.println();
               System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
               System.out.println();
               System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
               System.out.println();
               System.out.println   ("12. SECURING EMAIL CLIENTS."); 
               System.out.println();
               System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
               System.out.println();
               System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
               System.out.println();
               System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
            
               menuSelection = keyboard.nextInt();
            
               while (menuSelection < 1 || menuSelection > 17) 
               
               {
               
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();  
                  System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("HERE IS THE VALID LIST OF EMAIL-ISOLATION MAIN MENU CATEGORIES: ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
                  System.out.println();
                  System.out.println   ("2.  EMAIL STANDARDS ."); 
                  System.out.println();
                  System.out.println   ("3.  EMAIL SECURITY THREATS."); 
                  System.out.println();
                  System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
                  System.out.println();
                  System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
                  System.out.println();
                  System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
                  System.out.println();
                  System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
                  System.out.println();
                  System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
                  System.out.println();
                  System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
                  System.out.println();
                  System.out.println   ("12. SECURING EMAIL CLIENTS."); 
                  System.out.println();
                  System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
                  System.out.println();
                  System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
                  System.out.println();
                  System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 18) FROM THE LIST ABOVE: ");
               
               
               
                  menuSelection = keyboard.nextInt();
               
               } 
            
               break;
         
            case 5:
            
               EmailIsolationSetter MIP;
               MIP = new EmailIsolationSetter();
            
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.println("YOU SELECTED EMAIL-ISOLATION'S MALWARE-INCIDENTS-PREVENTION ");
               System.out.println();
               System.out.println("PLEASE SEE BELOW MALWARE-INCIDENTS-PREVENTION CATEGORIES ");
               System.out.println(); 
               System.out.println("1.  MALWARE-INCIDENTS-PREVENTION POLICY.");
               System.out.println();
               System.out.println("2.  MALWARE-INCIDENTS AWARENESS.");
               System.out.println();
               System.out.println("3.  MALWARE-INCIDENTS VULNERABILITY MITIGATION.");
               System.out.println();
               System.out.println("4.  MALWARE-INCIDENTS THREAT MITIGATION.");
               System.out.println();
               System.out.println("5.  MALWARE-INCIDENTS-PREVENTION & DEFENSIVE ARCHITECTURE.");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print(" ENTER YOUR CHOICE FROM MALWARE-INCIDENTS-PREVENTION CATEGORIES (1 to 5): ");
            
            
               menuSelect = keyboard.nextInt();
            
               while (menuSelect < 1 || menuSelect > 5)
               
               {
                  System.out.println("************************************************************************************************" );  
                  System.out.println("THIS IS INVALID CHOICE FOR MALWARE-INCIDENTS-PREVENTION CATEGORY SELECTION"); 
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW VALID MALWARE-INCIDENTS-PREVENTION SELECTIONS "); 
                  System.out.println();
                  System.out.println("1.  MALWARE-INCIDENTS-PREVENTION POLICY.");
                  System.out.println();
                  System.out.println("2.  MALWARE-INCIDENTS AWARENESS.");
                  System.out.println();
                  System.out.println("3.  MALWARE-INCIDENTS VULNERABILITY MITIGATION.");
                  System.out.println();
                  System.out.println("4.  MALWARE-INCIDENTS THREAT MITIGATION.");
                  System.out.println();
                  System.out.println("5.  MALWARE-INCIDENTS-PREVENTION & DEFENSIVE ARCHITECTURE.");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER YOUR CHOICE FROM MALWARE-INCIDENTS-PREVENTION CATEGORIES (1 to 5): ");
               
               
                  menuSelect = keyboard.nextInt();
               
               }
               if ( menuSelect == 1)
               
               {          
                  System.out.println();
                  System.out.println("MALWARE-INCIDENTS-PREVENTION-POLICY: ");
                  System.out.println();
               
               
                  MIP.setPLCY          ("Organizations should ensure that their policies address prevention of malware incidents. These policy\r\nstatements should be used as the basis for additional malware prevention efforts, such as user and IT staff\r\nawareness, vulnerability mitigation, threat mitigation, and defensive architecture.\r\nIf an organization does not state malware prevention considerations clearly in its policies, it is unlikely to perform malware prevention activities consistently and effectively \r\nthroughout the organization. Malware prevention–related policy should be as general as possible to\r\nprovide flexibility in policy implementation and to reduce the need for frequent policy updates, but also \r\nspecific enough to make the intent and scope of the policy clear. Although some organizations have \r\nseparate malware policies, many malware prevention considerations belong in other policies, such as\r\nacceptable use policies, so a separate malware policy might duplicate some of the content of other policies.\r\nMalware prevention–related policy should include provisions related to remote workers—both those using hosts controlled by the organization \r\nand those using hosts outside of the organization’s control (e.g., contractor computers, employees’ home computers, business partners’ computers, mobile devices).\r\n\r\nCommon malware prevention–related policy considerations include the following:\r\n\r\nRequiring the scanning of media from outside of the organization for malware before they can be used\r\n\r\nRequiring that email file attachments be scanned before they are opened\r\n\r\nProhibiting the sending or receipt of certain types of files (e.g., .exe files) via email\r\n\r\nRestricting or prohibiting the use of unnecessary software, such as user applications that are often used to transfer malware (e.g., personal use of external instant messaging and file sharing services)\r\n\r\nRestricting the use of removable media (e.g., flash drives), particularly on hosts that are at high risk of infection, such as publicly accessible kiosks\r\n\r\nSpecifying which types of preventive software (e.g., antivirus software, content filtering software) are required for each type of host (e.g., email server, web server, laptop, smart phone) and application (e.g., email client, web browser), and listing the high-level requirements for configuring and maintaining the software (e.g., software update frequency, host scan scope and frequency)\r\n\r\nRestricting or prohibiting the use of organization-issued and/or personally-owned mobile devices on the organization’s networks and for telework/remote access.");
               
               
                  System.out.println     ("" +  MIP.getPLCY());
                  System.out.println();          
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println( "TO CONTINUE WITH NEXT MALWARE-INCIDENTS-PREVENTION CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU  CHOICE # 5");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
               
               }
               
               else
               
                  if ( menuSelect == 2)
                  
                  {
                     System.out.println();
                     System.out.println();
                     System.out.println("AWARENESS: ");
                     System.out.println();
                  
                     MIP.setMIA ("An effective awareness program explains proper rules of behavior for use of an organization’s IT hosts \r\nand information. Accordingly, awareness programs should include guidance to users on malware incident prevention,  \r\nwhich can help reduce the frequency and severity of malware incidents. All users should be  \r\nmade aware of the ways in which malware enters and infects hosts; the risks that malware poses;  \r\nthe inability of technical controls to prevent all incidents; and the importance of users in preventing incidents,  \r\nwith an emphasis on avoiding social engineering attacks (as discussed below). In addition,  \r\nthe organization’s awareness program should cover the malware incident prevention considerations in the  \r\norganization’s policies and procedures, as described in Section 3.1, as well as generally recommended  \r\npractices for avoiding malware incidents. Examples of such practices are as follows: \r\n\r\nNot opening suspicious emails or email attachments, clicking on hyperlinks, etc. from unknown  \r\nor known senders, or visiting websites that are likely to contain malicious content \r\n\r\nNot clicking on suspicious web browser popup windows\r\n\r\nNot opening files with file extensions that are likely to be associated with malware (e.g., .bat, .com, .exe, .pif, .vbs)\r\n\r\nNot disabling malware security control mechanisms (e.g., antivirus software, content filtering \r\nsoftware, reputation software, personal firewall)\r\n\r\nNot using administrator-level accounts for regular host operation\r\n\r\nNot downloading or executing applications from untrusted sources.\r\n\r\norganizations should also make users aware of policies and procedures \r\nthat apply to malware incident handling, such as how to identify if a host may be infected, how to report a \r\nsuspected incident, and what users might need to do to assist with incident handling (e.g., updating \r\nantivirus software, scanning hosts for malware). Users should be made aware of how the organization will \r\ncommunicate notices of major malware incidents and given a way to verify the authenticity of all such notices. \r\nIn addition, users should be aware of changes that might be temporarily made to the environment \r\nto contain an incident, such as disconnecting infected hosts from networks.\r\n\r\nAs part of awareness activities, organizations should educate their users on the social engineering \r\ntechniques that are employed to trick users into disclosing information. Examples of recommendations for \r\navoiding phishing attacks and other forms of social engineering include:\r\n\r\n- Never reply to email requests for financial or personal information. Instead, contact the person or \r\nthe organization at the legitimate phone number or website. Do not use the contact information \r\nprovided in the email, and do not click on any attachments or hyperlinks in the email.\r\n\r\n- Do not provide passwords, PINs, or other access codes in response to emails or unsolicited popup windows. \r\nOnly enter such information into the legitimate website or application.\r\n\r\n- Do not open suspicious email file attachments, even if they come from known senders. If an \r\nunexpected attachment is received, contact the sender (preferably by a method other than email, \r\nsuch as phone) to confirm that the attachment is legitimate.\r\n\r\n- Do not respond to any suspicious or unwanted emails. (Asking to have an email address removed \r\nfrom a malicious party’s mailing list confirms the existence and active use of that email address, \r\npotentially leading to additional attack attempts.)\r\n\r\nAlthough user awareness programs are increasingly important to help reduce the frequency and severity \r\nof social engineering-driven malware incidents, the impact of these programs is still typically not as great \r\nas that of the technical controls described in incident prevention. An \r\norganization should not rely on user awareness as its primary method of preventing malware incidents;   , the awareness program should supplement the technical controls to provide additional protection against incidents.\r\n\r\nThe awareness program for users should also serve as the foundation for awareness activities for the IT \r\nstaff involved in malware incident prevention, such as security, system, and network administrators. \r\nAll IT staff members should have some basic level of awareness regarding malware prevention, and \r\nindividuals should be trained in the malware prevention–related tasks that pertain to their areas of responsibility. \r\nIn addition, on an ongoing basis, some IT staff members (most likely, some members of the \r\nsecurity or incident response teams) should receive and review bulletins on types of new malware \r\nthreats, assess the likely risk to the organization, and inform the necessary IT staff members of the new \r\nthreat so that incidents can be prevented.");
                  
                  
                  
                     System.out.println("" +  MIP.getMIA());  
                     System.out.println();
                     System.out.println("************************************************************************************************" );
                     System.out.println();
                     System.out.println( "TO CONTINUE WITH NEXT MALWARE-INCIDENTS-PREVENTION CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 5");
                     System.out.println();
                     System.out.println("************************************************************************************************" );   
                  
                  }
                  
                  else
                  
                     if ( menuSelect == 3 )
                     
                     {
                        System.out.println();
                        System.out.println();
                        System.out.println(" MALWARE-INCIDENTS-VULNERABILITY-MITIGATION: ");
                        System.out.println();  
                     
                        MIP.setMVM("Malware often attacks hosts by exploiting vulnerabilities in operating systems, \r\nservices, and applications. Consequently, mitigating vulnerabilities is very important to the prevention of \r\nmalware incidents, particularly when malware is released shortly after the announcement of a new \r\nvulnerability, or even before a vulnerability is publicly acknowledged. A vulnerability can usually be \r\nmitigated by one or more methods, such as applying patches to update the software or reconfiguring the \r\nsoftware (e.g., disabling a vulnerable service). Because of the challenges that vulnerability mitigation\r\npresents, including handling the continual discovery of new vulnerabilities, organizations should have presents, including handling the continual discovery of new vulnerabilities, organizations should \r\nhave documented policy, processes, and procedures for vulnerability mitigation.\r\n\r\nOrganizations should consider using security automation technologies with OS and application \r\nconfiguration checklists to help administrators secure hosts consistently and effectively. Security \r\nautomation technologies can use checklists to apply configuration settings that improve the default level \r\nautomation of security and to continuously monitor the hosts’ settings to verify that they are still in compliance with \r\nautomation the checklist settings.7 Organizations should also consider using security automation technologies for OS \r\nautomation and application patch management—to identify, acquire, distribute, and install security-related patches so \r\nas to mitigate vulnerabilities that the patches address.\r\n\r\nIn terms of security configurations, organizations should use sound host hardening principles. \r\nFor example, organizations should follow the principle of least privilege, which refers to configuring hosts \r\nto provide only the minimum necessary rights to the appropriate users, processes, and hosts. Least privilege \r\ncan be helpful in preventing malware incidents, because malware often requires administrator-level \r\nprivileges to exploit vulnerabilities successfully. If an incident does occur, prior application of least \r\nprivilege might minimize the amount of damage that the malware can cause. Organizations should also \r\nimplement other host hardening measures that can further reduce the possibility of malware incidents, such as the following:\r\n\r\n- Disabling or removing unneeded services (particularly network services), which are \r\nadditional vectors that malware can use to spread\r\n\r\n- Eliminating unsecured file shares, which are a common way for malware to spread\r\n\r\n- Removing or changing default usernames and passwords for OSs and applications, which could \r\nbe used by malware to gain unauthorized access to hosts\r\n\r\n- Disabling automatic execution of binaries and scripts, including AutoRun on Windows hosts\r\n\r\n- Changing the default file associations for file types that are most frequently used by malware \r\nbut not by users (e.g., .pif, .vbs) so that such files are not run automatically if users attempt to open them.\r\n\r\nHost hardening should also include applications, such as email clients, web browsers, and word processors, \r\nthat are frequently targeted by malware. Organizations should disable unneeded features and \r\ncapabilities from these applications, particularly those that are commonly exploited by malware, to limit \r\nthe possible attack vectors for malware. One example is the use of macro languages by word processors \r\nand spreadsheets; most common applications with macro capabilities offer macro security features that \r\npermit macros only from trusted locations or prompt the user to approve or reject each attempt to run a \r\nmacro, thus reducing the chance of macro-induced malware infection. Another example is preventing \r\nsoftware installation within web browsers by configuring browsers to prohibit plug-in installation or to \r\nprompt users to approve the installation of each plug-in.\r\n\r\nBeing able to alter application configuration settings quickly can be very beneficial in remediating \r\nvulnerabilities very quickly, including temporary remediation measures. For example, a configuration \r\nchange could disable a vulnerable service temporarily while the service’s vendor prepares and releases a \r\npatch that permanently fixes the vulnerability. Once the patch is available and deployed, the organization \r\ncan reverse the configuration change to reactivate the no longer vulnerable service. Organizations should \r\nconsider in advance how configuration settings could be changed in response to a malware emergency \r\nand establish and maintain appropriate procedures.");
                     
                        System.out.println("" +  MIP.getMVM());    
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                        System.out.println();
                        System.out.println( "TO CONTINUE WITH NEXT MALWARE-INCIDENTS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 5");
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                     
                     }
                     
                     else
                     
                        if ( menuSelect == 4)
                        
                        {
                           System.out.println();
                           System.out.println("THREAT-MITIGATION: ");
                           System.out.println();
                        
                           MIP.setMTM("Organizations should perform threat mitigation to detect and stop malware before it can affect its targets. \r\nEven if virtually all vulnerabilities in a host have been mitigated, threat mitigation is still critically \r\nimportant for example, for stopping instances of malware that do not exploit vulnerabilities, such as \r\nattacks that rely on social engineering methods to trick users into running malicious files. \r\nThreat mitigation is also critical for situations where a major new threat is likely to attack an organization soon \r\nand the organization does not have an acceptable vulnerability mitigation option. For example, there \r\nmight not be a patch available for a new vulnerability.\r\n\r\nSecurity tools that can mitigate malware threats: antivirus software, intrusion prevention systems (IPS), \r\nfirewalls, content filtering/inspection, and application whitelisting. For each of these categories, \r\nthe section also describes typical features, the types of malware and attack \r\nvectors the tools address, and the methods they use to detect and stop malware. Recommendations and \r\nguidance for implementing, configuring, and maintaining the tools are also provided, as well as\r\nexplanations of the tools’ shortcomings and the ways in which they complement other tools. In addition, \r\nthe section discusses client and server application settings that can be helpful in mitigating threats.\r\n\r\nAntivirus software is the most commonly used technical control for malware threat mitigation. \r\nThere are many brands of antivirus software, with most providing similar protection through the following recommended capabilities:\r\n\r\n- Scanning critical host components such as startup files and boot records.\r\n\r\n- Watching real-time activities on hosts to check for suspicious activity; a common example is \r\nscanning all email attachments for known malware as emails are sent and received. Antivirus\r\nsoftware should be configured to perform real-time scans of each file as it is downloaded, opened, \r\nor executed, which is known as on-access scanning.\r\n\r\n- Monitoring the behavior of common applications, such as email clients, web browsers, and \r\ninstant messaging software. Antivirus software should monitor activity involving the applications \r\nmost likely to be used to infect hosts or spread malware to other hosts.\r\n\r\n- Scanning files for known malware. Antivirus software on hosts should be configured to scan all \r\nhard drives regularly to identify any file system infections and, optionally, depending on \r\norganization security needs, to scan removable media inserted into the host before allowing its use. \r\nUsers should also be able to launch a scan manually as needed, which is known as on-demand scanning.\r\n\r\nIdentifying common types of malware as well as attacker tools.\r\n\r\n- Disinfecting files, which refers to removing malware from within a file, and quarantining files, \r\nwhich means that files containing malware are stored in isolation for future disinfection or \r\nexamination. Disinfecting a file is generally preferable to quarantining it because the malware is \r\nremoved and the original file restored; however, many infected files cannot be disinfected. \r\nAccordingly, antivirus software should be configured to attempt to disinfect infected files and to \r\neither quarantine or delete files that cannot be disinfected.\r\n\r\nOrganizations should use both host-based and network-based antivirus scanning. Organizations should \r\ndeploy antivirus software on all hosts for which satisfactory antivirus software is available. Antivirus \r\nsoftware should be installed as soon after OS installation as possible and then updated with the latest \r\nsignatures and antivirus software patches (to eliminate any known vulnerabilities in the antivirus software itself). \r\nThe antivirus software should then perform a complete scan of the host to identify any potential infections. \r\nTo support the security of the host, the antivirus software should be configured and maintained \r\nproperly so that it continues to be effective at detecting and stopping malware. Antivirus software is most \r\neffective when its signatures are fully up-to-date. Accordingly, antivirus software should be kept current \r\nwith the latest signature and software updates to improve malware detection.\r\n\r\nOrganizations should use centrally managed antivirus software that is controlled and monitored regularly \r\nby antivirus administrators, who are also typically responsible for acquiring, testing, approving, and \r\ndelivering antivirus signature and software updates throughout the organization. Users should not be able \r\nto disable or delete antivirus software from their hosts, nor should they be able to alter critical settings. \r\nAntivirus administrators should perform continuous monitoring to confirm that hosts are using current \r\nantivirus software and that the software is configured properly. Implementing all of these \r\nrecommendations should strongly support an organization in having a strong and consistent antivirus \r\ndeployment across the organization.\r\n\r\nA possible measure for improving malware prevention is to use multiple antivirus products for key hosts, \r\nsuch as email servers. For example, one antivirus vendor might have a new signature available several \r\nhours before another vendor, or an organization might have an operational issue with a particular \r\nsignature update. Another possibility is that an antivirus product itself might contain an exploitable vulnerability; \r\nhaving an alternative product available in such cases could provide protection until the issue \r\nwith the primary product has been resolved. Because running multiple antivirus products on a single host \r\nsimultaneously is likely to cause conflicts between the products, if multiple products are used concurrently, \r\nthey should be installed on separate hosts. For example, one antivirus product could be used on perimeter \r\nemail servers and another on internal email servers. This could provide more effective \r\ndetection of new threats, but also would necessitate increased administration and training, as well as \r\nadditional hardware and software costs.\r\n\r\nAlthough antivirus software has become a necessity for malware incident prevention, it is not possible \r\nfor antivirus software to stop all malware incidents. As discussed previously in this section, antivirus \r\nsoftware does not excel at stopping previously unknown threats. Antivirus software products detect \r\nmalware primarily by looking for certain characteristics of known instances of malware. This is highly \r\neffective for identifying known malware, but is not so effective at detecting the highly customized, tailored malware increasingly being used.");
                        
                           System.out.println("" + MIP.getMTM());      
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                           System.out.println();
                           System.out.println( "TO CONTINUE WITH NEXT MALWARE-INCIDENTS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 5");
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                        
                        }
                        
                        else
                        
                           if ( menuSelect == 5)
                           
                           {
                              System.out.println();         
                              System.out.println();
                              System.out.println("MALWARE-INCIDENTS-PREVENTION-&-DEFENSIVE-ARCHITECTURE: "); 
                              System.out.println();     
                           
                           
                              MIP.setMIDA("Network-based intrusion prevention systems (IPS) perform packet sniffing and analyze network traffic to \r\nidentify and stop suspicious activity.9 Network-based IPS products are typically deployed inline, which \r\nmeans that the software acts like a network firewall. It receives packets, analyzes them, and allows \r\nacceptable packets to pass through. The network-based IPS architecture allows some attacks to be \r\ndetected on networks before they reach their intended targets. Most network-based IPS products use a \r\ncombination of attack signatures and analysis of network and application protocols, which means that \r\nthey compare network activity for frequently attacked applications (e.g., email servers, web servers) to expected behavior to identify potentially malicious activity.\r\n\r\nFirewalls\r\n\r\nA network firewall is a device deployed between networks to restrict which types of traffic can pass from one network to another. A host-based firewall is a piece of software running on a single host that can restrict incoming and outgoing network activity for that host only. Both types of firewalls can be useful for preventing malware incidents. Organizations should configure their firewalls with deny by default rulesets, meaning that the firewalls deny all incoming traffic that is not expressly permitted. With such rulesets in place, malware could not spread using services deemed unnecessary to the organization.11 Organizations should also restrict outgoing traffic to the degree feasible, with a focus on preventing the use of prohibited services commonly used by malware.\r\n\r\nnetworks to restrict which types of traffic can pass from \r\none network to another. A host-based firewall is a piece of software running on a single host that can \r\nrestrict incoming and outgoing network activity for that host only. Both types of firewalls can be useful \r\nfor preventing malware incidents. Organizations should configure their firewalls with deny by default \r\nrulesets, meaning that the firewalls deny all incoming traffic that is not expressly permitted. With such \r\nrulesets in place, malware could not spread using services deemed unnecessary to the organization. \r\nOrganizations should also restrict outgoing traffic to the degree feasible, with a focus on preventing the \r\nuse of prohibited services commonly used by malware.\r\n\r\nContent-Filtering/Inspection:\r\n\r\nOrganizations should use spam filtering technologies to reduce the amount of spam that reaches \r\nusers. Spam is often used for malware delivery, particularly phishing attacks, so reducing spam \r\nshould lead to a corresponding decline in spam-triggered malware incidents. Organizations should also consider \r\nconfiguring their email servers and clients to block attachments with file extensions that are associated \r\nwith malicious code (e.g., .pif, .vbs), and suspicious file extension combinations (e.g., .txt.vbs, .htm.exe). \r\nHowever, this might also inadvertently block legitimate activity. Some organizations alter suspicious \r\nemail attachment file extensions so that a recipient would have to save the attachment and rename it \r\nbefore running it, which can be a good compromise between functionality and security.\r\n\r\nOrganizations should also use content inspection and filtering technologies for stopping web-based \r\nmalware threats. Web content filtering software has several ways of doing this; although it is typically \r\nthought of as preventing access to materials that are inappropriate for the workplace, it may also contain \r\nblacklist and reputation information (see below). It can also block undesired file types, such as by file \r\nextension or by mobile code type. For particularly high security situations, organizations should consider\r\nrestricting which types of mobile code (such as unsigned ActiveX) may or may not be used from various \r\nsources (e.g., internal servers, external servers).\r\n\r\nOrganizations should also block undesired web browser popup windows, as a form of content filtering. \r\nSome popup windows are crafted to look like legitimate system message boxes or websites, and can trick \r\nusers into going to phony websites, including sites used for phishing, or authorizing changes to their \r\nhosts, among other malicious actions. Most web browsers can block popup windows, and third-party \r\npopup blockers are also available.\r\n\r\nBoth email and web content filtering should use real-time blacklists, reputation services, and other similar \r\nmechanisms whenever feasible to avoid accepting content from known or likely malicious hosts and \r\ndomains. These mechanisms use a variety of techniques to identify certain IP addresses, domain names, \r\nor URIs as being probably malicious or probably benign. Real-time blacklists tend to be based on \r\nobserved malware activity, while reputation services may be based on user opinions or on automated \r\nanalysis of websites, emails, etc. without necessarily detecting malware. Because the fidelity and \r\naccuracy of these mechanisms varies widely from one implementation to another, organizations should \r\ncarefully evaluate any real-time blacklists, reputation services, or other similar mechanisms before \r\ndeploying them into production environments to minimize disruption to operations.\r\n\r\nApplication Whitelisting\r\n\r\nApplication whitelisting technologies, also known as application control programs, are used to specify \r\nwhich applications are authorized for use on a host. Most application whitelisting technologies can be run \r\nin two modes: audit and enforcement. In enforcement mode, the technology generally prohibits all \r\napplications that are not in the whitelist from being executed. In audit mode, the technology logs all \r\ninstances of non-whitelisted applications being run on the host, but does not act to stop them. The tradeoff \r\nbetween enforcement mode and audit mode is simple; using enforcement mode will stop malware from \r\nexecuting, but it may also prevent benign applications not included on the whitelist from being run. \r\nOrganizations deploying application whitelisting technologies should consider first deploying them in \r\naudit mode, so as to identify any necessary applications missing from the whitelist, before reconfiguring \r\nthem for enforcement mode. Running application whitelisting technologies in audit mode is analogous to \r\nintrusion detection software without intrusion prevention capabilities; it can be useful after an infection \r\noccurs to determine which hosts were affected, but it has no ability to prevent infections.\r\n\r\nOrganizations with high security needs or high-risk environments should consider the use of application \r\nwhitelisting technologies for their managed hosts. Application whitelisting technologies are built into \r\nmany operating systems and are also available through third-party utilities.\r\n\r\nDefensive Architecture.\r\n\r\nNo matter how rigorous vulnerability and threat mitigation efforts are, malware incidents will still occur. \r\nThere are four types of complementary methods that organizations should consider using to \r\nalter the defensive architecture of a host’s software so as to reduce the impact of incidents: BIOS \r\nprotection, sandboxing, browser separation, and segregation through virtualization.\r\n\r\nBIOS Protection\r\nUnauthorized modification of BIOS firmware by malicious software constitutes a significant threat \r\nbecause of the BIOS’s unique and privileged position within the PC architecture. A malicious BIOS \r\nmodification could be part of a sophisticated, targeted attack on an organization—either a permanent \r\ndenial of service (if the BIOS is corrupted) or a persistent malware presence (if the BIOS is implantedwith malware). \r\nThe move from conventional BIOS implementations to implementations based on the \r\nUnified Extensible Firmware Interface (UEFI) may make it easier for malware to target the BIOS in a \r\nwidespread fashion, as these BIOS implementations are based on a common specification.\r\n\r\nSandboxing\r\n\r\nSandboxing refers to a security model where applications are run within a sandbox—a controlled \r\nenvironment that restricts what operations the applications can perform and that isolates them from other \r\napplications running on the same host. In a sandbox security model, typically only authorized “safe” \r\noperations may be performed within the sandbox; the sandbox prohibits applications within the sandbox \r\nfrom performing any other operations. The sandbox also restricts access to system resources, such as \r\nmemory and the file system, to keep the sandbox’s applications isolated from the host’s other applications.\r\n\r\nSandboxing provides several benefits in terms of malware incident prevention and handling. By limiting \r\nthe operations available, it can prevent malware from performing some or all of the malicious actions it is \r\nattempting to execute; this could prevent the malware from succeeding or reduce the damage it causes. \r\nAnd the sandboxing environment—the isolation—can further reduce the impact of the malware by \r\nrestricting what information and functions the malware can access. Another benefit of sandboxing is that \r\nthe sandbox itself can be reset to a known good state every time it is initialized.\r\n\r\nBrowser Separation\r\n\r\nMultiple brands of Web browsers (e.g., Microsoft Internet Explorer, Mozilla Firefox, Apple Safari, \r\nGoogle Chrome, Opera) can be installed on a single host. Accessing Web sites containing malicious \r\ncontent is one of the most common ways for hosts to be attacked, such as malicious plug-ins being \r\ninstalled within a browser. To reduce the impact of such attacks, users can use one brand of browser for \r\ncorporate applications and another brand of browser for all other website access. This separates the \r\nsensitive corporate data within one browser from the data within the other browser, providing better \r\nprotection for the corporate data (although this alone cannot adequately secure browser data) and reducing \r\nthe likelihood that malware encountered during general web browsing will affect corporate applications. \r\nHaving a separate brand of browser for corporate applications also allows that browser to be secured more \r\ntightly, such as disabling all forms of mobile code (e.g., Java, ActiveX) that are not required for the specified applications.\r\n\r\nSegregation Through Virtualization\r\n\r\nBrowser separation essentially segregates web browsers from each other. Virtualization can be used to \r\nsegregate applications or operating systems from each other, with much more rigor than simple browser \r\nseparation can provide. For example, an organization could have one OS instance for corporate \r\napplications and another OS instance for all other activities, including web browsing. Each OS instance is \r\na known-good virtualized image that contains the appropriate applications and is secured accordingly. \r\nThe user loads these virtualized images and does their work within these guest OS images, not directly on \r\nthe host OS itself. A compromise occurring within one image will not affect the other image unless the\r\ncompromise involves the virtualization software itself. Another benefit is that every time an image is \r\nrestarted, it can be reloaded from the known-good image, ensuring that any compromises occurring within the image are eradicated.\r\n\r\nAn alternative strategy, more usable but less secure, is to use a guest OS for more risky behavior (such as \r\ngeneral web browsing) and the host OS for corporate applications. This helps to isolate the riskier \r\nactivities from the other activities on the host. The host OS can be restricted to only whitelisted \r\napplications to prevent unauthorized applications from being run within it.");
                           
                           
                              System.out.println("" + MIP.getMIDA());
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                              System.out.println();
                              System.out.println( "TO CONTINUE WITH NEXT MALWARE-INCIDENTS-PREVENTION CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 5");
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                           
                           }
                           
                           else
                           
                              System.out.println();
               System.out.println   ("HERE ARE EMAIL-ISOLATION-FRAMEWORK MAIN MENU CATEGORIES LIST: ");
               System.out.println();
               System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
               System.out.println();
               System.out.println   ("2.  EMAIL STANDARDS ."); 
               System.out.println();
               System.out.println   ("3.  EMAIL SECURITY THREATS."); 
               System.out.println();
               System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
               System.out.println();
               System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
               System.out.println();
               System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
               System.out.println();
               System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
               System.out.println();
               System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
               System.out.println();
               System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
               System.out.println();
               System.out.println   ("12. SECURING EMAIL CLIENTS."); 
               System.out.println();
               System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
               System.out.println();
               System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
               System.out.println();
               System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
            
               menuSelection = keyboard.nextInt();
            
               while (menuSelection < 1 || menuSelection > 17) 
               
               {
               
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();  
                  System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("HERE IS THE VALID LIST OF EMAIL-ISOLATION MAIN MENU CATEGORIES: ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
                  System.out.println();
                  System.out.println   ("2.  EMAIL STANDARDS ."); 
                  System.out.println();
                  System.out.println   ("3.  EMAIL SECURITY THREATS."); 
                  System.out.println();
                  System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
                  System.out.println();
                  System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
                  System.out.println();
                  System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
                  System.out.println();
                  System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
                  System.out.println();
                  System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
                  System.out.println();
                  System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
                  System.out.println();
                  System.out.println   ("12. SECURING EMAIL CLIENTS."); 
                  System.out.println();
                  System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
                  System.out.println();
                  System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
                  System.out.println();
                  System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
               
               
               
                  menuSelection = keyboard.nextInt();
               
               } 
            
               break;
         
            case 6:
            
               EmailIsolationSetter MIR;
               MIR = new EmailIsolationSetter();
            
            
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println("YOU SELECTED MALWARE-INCIDENT-RESPONSE CATEGORY FROM EMAIL-ISOLATION MAIN MENU ");
               System.out.println();
               System.out.println("PLEASE SEE BELOW MALWARE-INCIDENT-RESPONSE CATEGORIES: ");
               System.out.println(); 
               System.out.println("1.  MALWARE-INCIDENT-RESPONSE PREPARATION.");
               System.out.println();
               System.out.println("2.  MALWARE-INCIDENT DETECTION AND ANALYSIS.");
               System.out.println();
               System.out.println("3.  MALWARE-INCIDENT CONTAINMENT.");
               System.out.println();
               System.out.println("4.  MALWARE-INCIDENT ERADICATION.");
               System.out.println();
               System.out.println("5.  MALWARE-INCIDENT RECOVERY.");
               System.out.println();
               System.out.println("6.  MALWARE-INCIDENT LESSONS LEARNED.");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER YOUR CHOICE MALWARE-INCIDENT-RESPONSE CATEGORIES (1 to 6): ");
            
            
               menuSelect = keyboard.nextInt();
            
               while (menuSelect < 1 || menuSelect > 6)
               
               {
               
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println("THIS IS INVALID CHOICE FOR MALWARE-INCIDENT-RESPONSE SELECTION "); 
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW VALID MALWARE-INCIDENT-RESPONSE SELECTIONS:");
                  System.out.println();
                  System.out.println("1.  MALWARE-INCIDENT-RESPONSE PREPARATION.");
                  System.out.println();
                  System.out.println("2.  MALWARE-INCIDENT DETECTION AND ANALYSIS.");
                  System.out.println();
                  System.out.println("3.  MALWARE-INCIDENT CONTAINMENT.");
                  System.out.println();
                  System.out.println("4.  MALWARE-INCIDENT ERADICATION.");
                  System.out.println();
                  System.out.println("5.  MALWARE-INCIDENT-RESPONSE RECOVERY.");
                  System.out.println();
                  System.out.println("6.  MALWARE-INCIDENT LESSONS LEARNED.");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print(" ENTER YOUR CHOICE MALWARE-INCIDENT-RESPONSE CATEGORIES (1 to 6): ");
               
               
               
                  menuSelect = keyboard.nextInt();
               
               }
            
               System.out.println();
            // System.out.println(" NOTE: There are eight performance attributes, or currencies, to be considered when evaluating whether a EMAIL-ISOLATION network can deliver on its full potential.".toUpperCase());
            // System.out.println();                
            //System.out.println(" NOTE:  Without all eight of these currencies, you don’t have a true EMAIL-ISOLATION network. With them, you have a powerful, game-changing platform for innovation .".toUpperCase());
            //System.out.println(); 
            
               if ( menuSelect == 1)
               
               {          
                  System.out.println();
                  System.out.println("MALWARE-INCIDENT-RESPONSE PREPARATION: ");
                  System.out.println();
               
               
                  MIR.setMIRP           ("Organizations should perform preparatory measures to ensure that they are capable of responding \r\neffectively to malware incidents. Information below will describe several recommended preparatory \r\nmeasures, including building and maintaining malware-related skills within the incident response team, \r\nfacilitating communication and coordination throughout the organization, and acquiring necessary tools and resources.\r\n\r\nBuilding and Maintaining Malware-Related Skills\r\n\r\nIn addition to standard incident response team skills as described in NIST SP 800-61, \r\nall malware incident handlers should have a solid understanding of how each major category of malware infects hosts \r\nand spreads. Also, incident handlers should be familiar with the organization’s implementations and \r\nconfigurations of malware detection tools so that they are better able to analyze supporting data and \r\nidentify the characteristics of threats.\r\n\r\nFacilitating Communication and Coordination\r\n\r\nOne of the most common problems during malware incident handling is poor communication and coordination. \r\nAnyone involved in an incident, including users, can inadvertently cause additional \r\nproblems because of a limited view or understanding of the situation. To improve communication and \r\ncoordination, an organization should designate in advance a few individuals or a small team to be \r\nresponsible for coordinating the organization’s responses to malware incidents. The coordinator’s primary \r\ngoal is to maintain situational awareness by gathering all pertinent information, making decisions that are \r\nin the best interests of the organization, and communicating pertinent information and decisions to all \r\nrelevant parties in a timely manner. For malware incidents, the relevant parties often include end users, \r\nwho might be given instructions on how to avoid infecting their hosts, how to recognize the signs of an \r\ninfection, and what to do if a host appears to be infected. The coordinator also needs to provide technical \r\nguidance and instructions to all staff assisting with containment, eradication, and recovery efforts, as well \r\nas giving management regular updates on the status of the response and the current and likely future \r\nimpact of the incident. Another possible role for the coordinator is interacting with external parties, such \r\nas other incident response teams facing similar malware issues.\r\n\r\nOrganizations should also establish a point of contact for answering questions about the legitimacy of \r\nmalware alerts. Many organizations use the IT help desk as the initial point of contact and give help desk \r\nagents access to sources of information on real malware threats and virus hoaxes so that they can quickly \r\ndetermine the legitimacy of an alert and provide users with guidance on what to do. Organizations should \r\ncaution users not to forward malware alerts to others without first confirming that the alerts are legitimate.\r\n\r\nAcquiring Tools and Resources\r\n\r\nOrganizations should also ensure that they have the necessary tools (hardware and software) and resources to assist in malware incident handling.");              
                  System.out.println        ("" +  MIR.getMIRP());
                  System.out.println();          
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println( "TO CONTINUE WITH NEXT MALWARE-INCIDENT-RESPONSE CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU  CHOICE # 6");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
               
               }
               
               else
               
                  if ( menuSelect == 2)
                  
                  {
                     System.out.println();
                     System.out.println();
                     System.out.println("DETECTION-AND-ANALYSIS: ");
                     System.out.println();
                  
                     MIR.setMIRDA       ("Organizations should strive to detect and validate malware incidents rapidly to minimize the number of \r\ninfected hosts and the amount of damage the organization sustains. Because malware can take many \r\nforms and be distributed through many means, there are many possible signs of a malware incident and \r\nmany locations within an organization where the signs might be recorded or observed. It sometimes takes \r\nconsiderable analysis, requiring extensive technical knowledge and experience, to confirm that an \r\nincident has been caused by malware, particularly if the malware threat is new and unknown. After \r\nmalware incident detection and validation, incident handlers should determine the type, extent, and \r\nmagnitude of the problem as quickly as possible so that the response to the incident can be given the \r\nappropriate priority. Sections 4.2.1 through 4.2.4 provide guidance on identifying the characteristics of \r\nincidents, identifying infected hosts, prioritizing incident response efforts, and analyzing malware, respectively.\r\n\r\nIdentifying Malware Incident Characteristics\r\n\r\nBecause no indicator is completely reliable—even antivirus software might miscategorize benign activity \r\nas malicious—incident handlers need to analyze any suspected malware incident and validate that \r\nmalware is the cause. In some cases, such as a massive, organization-wide infection, validation may be \r\nunnecessary because the nature of the incident is obvious. The goal is for incident handlers to be as \r\ncertain as feasible that an incident is caused by malware and to have a basic understanding of the type of \r\nmalware threat responsible, such as a worm or a Trojan horse. If the source of the incident cannot easily \r\nbe confirmed, it is often better to respond as if it were caused by malware and to alter response efforts if it \r\nis later determined that malware is not involved. Waiting for conclusive evidence of malware might have \r\na serious negative impact on response efforts and significantly increase the damage sustained by the organization.\r\n\r\nAs part of the analysis and validation process, incident handlers typically identify characteristics of the \r\nmalware activity by examining detection sources. Understanding the activity’s characteristics is very \r\nhelpful in assigning an appropriate priority to the incident response efforts and planning effective \r\ncontainment, eradication, and recovery activities. Incident handlers should collaborate with security \r\nadministrators in advance to identify data sources that can aid in detecting malware information and to \r\nunderstand what types of information each data source may record. In addition to the obvious sources of \r\ndata, such as antivirus software, intrusion detection system (IDS), and security information and event (SIEM) technologies, incident handlers should be aware of and use secondary sources as \r\nappropriate. See Section 4.2 for more information on possible sources of malware characteristic information.\r\n\r\nOnce incident handlers have reviewed detection source data and identified characteristics of the malware, \r\nthe handlers could search for those characteristics in antivirus vendors’ malware databases and identify \r\nwhich instance of malware is the most likely cause. If the malware has been known for some time, it is \r\nlikely that antivirus vendors will have a substantial amount of information on it, such as the following:\r\n\r\n- Malware category (e.g., virus, worm, Trojan horse)\r\n\r\n- Services, ports, protocols, etc. that are attacked\r\n\r\n- Vulnerabilities that are exploited (e.g., software flaws, misconfigurations, social engineering)\r\n\r\n- Malicious filenames, sizes, content, and other metadata (e.g., email subjects, web URLs)\r\n\r\n- Which versions of operating systems, devices, applications, etc., may be affected\r\n\r\n- How the malware affects the infected host, including the names and locations of affected file,\r\naltered configuration settings, installed backdoor ports, etc.\r\n\r\n- How the malware propagates and how to approach containment\r\n\r\n- How to remove the malware from the host.\r\n\r\nUnfortunately, the newest threats might not be included in malware databases for several hours or days, \r\ndepending on the relative importance of the threat, and highly customized threats might not be included in \r\nmalware databases at all. Therefore, incident handlers may need to consult other sources of information. \r\nOne option is using public security mailing lists, which might contain first-hand accounts of malware incidents; \r\nhowever, such reports are often incomplete or inaccurate, so incident handlers should validate \r\nany information obtained from these sources. Another potentially valuable source of malware \r\ncharacteristic information is peers at other organizations. Other organizations may have already been \r\naffected and gathered data on the threat. Establishing and maintaining good relationships with peers at \r\nother organizations that face similar problems can be advantageous for all involved. An alternative source \r\nof information is self-discovery by performing malware analysis. This is particularly \r\nimportant if the malware is highly customized; there may be no other way of getting details for the \r\nmalware other than doing a hands-on analysis.\r\n\r\nIdentifying Infected Hosts\r\n\r\nIdentifying hosts that are infected by malware is part of every malware incident. Once identified, infected \r\nhosts can undergo the appropriate containment, eradication, and recovery actions. Unfortunately, \r\nidentifying all infected hosts is often complicated by the dynamic nature of computing. For instance, \r\npeople shut hosts down, disconnect them from networks, or move them from place to place, making it \r\nextremely difficult to identify which hosts are currently infected. In addition, some hosts can boot to \r\nmultiple OSs or use virtual operating system software; an infection in one OS instantiation might not be \r\ndetectable when a host is currently using another OS.\r\n\r\nAccurate identification of infected hosts can also be complicated by other factors. For example, hosts with \r\nunmitigated vulnerabilities might be disinfected and reinfected multiple times. Some instances of \r\nmalware actually remove some or all traces of other malware, which could cause the partially or fully \r\nremoved infections to go undetected. In addition, the data concerning infected hosts might come from \r\nseveral sources—antivirus software, IDSs, SIEMs, user reports, and other methods—and be very difficult \r\nto consolidate and keep current.\r\n\r\nForensic Identification\r\n\r\nForensic identification is the practice of identifying infected hosts by looking for evidence of recent \r\ninfections. The evidence may be very recent (only a few minutes old) or not so recent (hours or days old); \r\nthe older the information is, the less accurate it is likely to be. The most obvious sources of evidence are \r\nthose that are designed to identify malware activity, such as antivirus software, content filtering (e.g., anti-spam measures), \r\nIPS, and SIEM technologies. The logs of security applications might contain detailed \r\nrecords of suspicious activity, and might also indicate whether a security compromise occurred or \r\nwas prevented.\r\n\r\nIn situations in which the typical sources of evidence do not contain the necessary information, \r\norganizations might need to turn to secondary sources, such as the following:\r\n\r\n-n- DNS Server Logs. DNS server logs often contain records of infected hosts attempting to \r\nget the IP address for an external malicious site that they are trying to interact with (e.g., send data to, \r\nreceive commands from). Some organizations deploy passive DNS collection systems, which \r\nkeep track of all DNS resolutions occurring within the enterprise; these are often more helpful \r\nthan DNS server logs in identifying malicious activity because malware might use DNS services \r\nother than the organization’s. Analysts should be cautious of blocking hosts based only on \r\nresolved IP addresses because many current attacks use fast flux DNS, which means that each \r\ndomain resolves to several different IP addresses (in a round robin arrangement), and these \r\naddresses often change in a matter of hours. The newer the DNS resolution, the more likely the IP \r\naddresses are to be the correct ones to block in the short term.\r\n\r\n- Other Application Server Logs. Applications commonly used as malware transmission \r\nmechanisms, such as email and HTTP, might record information in their logs that indicates which \r\nhosts were infected. From end to end, information regarding a single email message might be \r\nrecorded in several places: the sender’s host, each email server that handles the message, and the \r\nrecipient’s host, as well as antivirus and content filtering servers. Similarly, hosts running web \r\nbrowsers can provide a rich resource for information on malicious web activity, including a \r\nhistory of websites visited and the dates and times that they were visited, and cached web data files.\r\n\r\n- Network Forensic Tools. Software programs that capture and record packets, such as network \r\nforensic analysis tools and packet sniffers, might have highly detailed information on malware \r\nactivity. However, because these tools record so much information about most or all network \r\nactivity, it can be very time-intensive to extract just the needed information. More efficient means \r\nof identifying infected hosts are often available.\r\n\r\n- Network Device Logs. Firewalls, routers, and other filtering devices that record connection \r\nactivity, as well as network monitoring tools, might be helpful in identifying network connection \r\nactivity (e.g., specific port number combinations, unusual protocols) consistent with certain malware.\r\n\r\nUsing forensic data for identifying infected hosts can be advantageous over other methods because the \r\ndata has already been collected—the pertinent data just needs to be extracted from the total data set. \r\nUnfortunately, for some data sources, extracting the data can take a considerable amount of time. Also, \r\nevent information can become outdated quickly, causing uninfected hosts to undergo containment \r\nunnecessarily and allowing infected hosts to avoid containment measures. If an accurate, comprehensive, \r\nand reasonably current source of forensic data is available, it might provide the most effective way of \r\nidentifying infected hosts.\r\n\r\nActive Identification\r\nActive identification methods are used to identify which hosts are currently infected. Immediately after\r\nidentifying an infection, some active approaches can be used to perform containment and eradication\r\nmeasures for the host, such as running a disinfection utility, deploying patches or antivirus updates, or\r\nmoving the host to a VLAN for infected hosts. Active identification can be performed through several\r\nmethods, including the following:\r\n\r\n- Security Automation. Security automation technologies, particularly those used for continuous\r\nmonitoring (e.g., network access control technologies), can be used to check host characteristics\r\nfor signs of a current infection, such as a particular configuration setting or a system file with a\r\ncertain size that indicates an infection. Security automation technologies are generally the\r\npreferred method for active identification.\r\n\r\n- Custom Network-Based IPS or IDS Signature. Writing a custom IPS or IDS signature that\r\nidentifies infected hosts is often a highly effective technique. Some organizations have separate\r\nIPS or IDS sensors with strong signature-writing capabilities that can be dedicated to identifying\r\nmalware infections. This provides a high-quality source of information while keeping other\r\nsensors from becoming overloaded with malware alerts.\r\n\r\n- Packet Sniffers and Protocol Analyzers. Configuring packet sniffers and protocol analyzers to\r\nlook only for network traffic matching the characteristics of a particular malware threat can be\r\neffective at identifying infected hosts. An example of what to monitor is to look for botnet\r\ncommand and control communications being carried over IRC. These packet examination\r\ntechniques are most helpful if most or all malware-generated network traffic attempts to pass\r\nthrough the same network device or a few devices.\r\n\r\nAlthough active approaches can produce highly accurate results, active approaches need to be used\r\nrepeatedly because the status of infections changes constantly and the data is gathered over a period of time.\r\n\r\nManual Identification\r\n\r\nAnother method for identifying infected hosts is the manual approach. This is by far the most laborintensive \r\nof the three methods. It should only be considered in those situations where automated methods\r\nare not feasible, such as when networks are completely overwhelmed by infection-related traffic using\r\nspoofed addresses. Also, if users have full control over their hosts, as they do in many non-managed\r\nenvironments, the characteristics of hosts may be so different that the results of automated identification\r\nmethods are quite incomplete and inaccurate. In such situations, a manual approach might be needed to\r\nsupplement automated approaches.\r\n\r\nIdentification Recommendations\r\n\r\nAlthough active approaches typically produce the most accurate results, they are often not the fastest way\r\nof identifying infections. It might take considerable time to scan every host in an organization, and\r\nbecause hosts that have been disconnected or shut off will not be identified, the scan will need to be\r\nrepeated. If forensic data is very recent, it might be a good source of readily available information,\r\nalthough the information might not be comprehensive. Manual methods are generally not feasible for\r\ncomprehensive enterprise-wide identification, but they are a necessary part of identification when other\r\nmethods are not sufficient. In many cases, it is most effective to use multiple approaches simultaneously\r\nor in sequence to provide the best results.\r\n\r\nPrioritizing Incident Response\r\n\r\nOnce a malware incident has been validated, the next activity is to prioritize its handling.\r\npresents general guidelines for incident prioritization; this section extends those by including additional\r\nfactors to consider during prioritization.\r\n\r\nCertain forms of malware, such as worms, tend to spread very quickly and can cause a substantial impact\r\nin minutes or hours, so they often necessitate a high-priority response. Other forms of malware, such as\r\nTrojan horses, tend to affect a single host; the response to such incidents should be based on the value of\r\nthe data and services provided by the host. Organizations should establish a set of criteria that identify the\r\nappropriate level of response for various malware-related situations. The criteria should incorporate\r\nconsiderations such as the following:\r\n\r\n- How the malware entered the environment and what transmission mechanisms it uses\r\n\r\n- What type of malware it is (e.g., virus, worm, Trojan horse)\r\n\r\n- Which types of attacker tools are placed onto the host by the malware\r\n\r\n- What networks and hosts the malware is affecting and how it is affecting them\r\n\r\n- How the impact of the incident is likely to increase in the following minutes, hours, and days if\r\nthe incident is not contained.\r\n\r\nMalware Analysis\r\n\r\nIncident handlers can study the behavior of malware by analyzing it either actively (executing the\r\nmalware) or forensically (examining the infected host for evidence of malware). Forensic approaches are\r\nsafer to perform on an infected host because they can examine the host without allowing the malware to\r\ncontinue executing. However, sometimes it is significantly faster and easier to analyze malware by\r\nmonitoring it during execution. Such active approaches are best performed on malware test systems\r\ninstead of production hosts, to minimize possible damage caused by allowing the malware to execute. ");
                     System.out.println ("" +  MIR.getMIRDA());
                     System.out.println();
                     System.out.println("************************************************************************************************" );
                     System.out.println();
                     System.out.println( "TO CONTINUE WITH NEXT MALWARE-INCIDENT CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 6");
                     System.out.println();
                     System.out.println("************************************************************************************************" );   
                  
                  }
                  
                  else
                  
                     if ( menuSelect == 3 )
                     
                     {
                        System.out.println();
                        System.out.println();
                        System.out.println("MALWARE-INCIDENT-CONTAINMENT: ");
                        System.out.println();  
                     
                        MIR.setMIRC("Containment\r\n\r\nContainment of malware has two major components: stopping the spread of the malware and preventing\r\nfurther damage to hosts. Nearly every malware incident requires containment actions. In addressing an\r\nincident, it is important for an organization to decide which methods of containment to employ initially,\r\nearly in the response. Containment of isolated incidents and incidents involving noninfectious forms of\r\nmalware is generally straightforward, involving such actions as disconnecting the affected hosts from\r\nnetworks or shutting down the hosts. For more widespread malware incidents, such as fast-spreading\r\nworms, organizations should use a strategy that contains the incident for most hosts as quickly as\r\npossible; this should limit the number of machines that are infected, the amount of damage that is done,\r\nand the amount of time that it will take to fully recover all data and services.\r\n\r\nContainment methods can be divided into four basic categories: relying on user participation, performing\r]\nautomated detection, temporarily halting services, and blocking certain types of network connectivity.\r\n\r\nContainment Through User Participation\r\n\r\nAt one time, user participation was a valuable part of containment efforts, particularly during large-scale\r\nincidents in non-managed environments. Users were provided with instructions on how to identify\r\ninfections and what measures to take if a host was infected, such as calling the help desk, disconnecting\r\nthe host from the network, or powering off the host. The instructions might also cover malware\r\neradication, such as updating antivirus signatures and performing a host scan, or obtaining and running a\r\nspecialized malware eradication utility. As hosts have increasingly become managed, user participation in\r\ncontainment has sharply decreased. However, having users perform containment actions is still helpful in\r\nnon-managed environments and other situations in which use of fully automated containment methods\r\nis not feasible.\r\n\r\nContainment Through Automated Detection\r\nMany malware incidents can be contained primarily through the use of the automated technologies\r\nfor preventing and detecting infections. These technologies include antivirus\r\nsoftware, content filtering, and intrusion prevention software. Because antivirus software on hosts can\r\ndetect and remove infections, it is often the preferred automated detection method for assisting in\r\ncontainment. However, as previously discussed, many of today’s malware threats are novel, so antivirus\r\nsoftware and other technologies often fail to recognize them as being malicious. Also, malware that\r\ncompromises the OS may disable security controls such as antivirus software, particularly in unmanaged\r\nenvironments where users have greater control over their hosts. Containment through antivirus software is\r\nnot as robust and effective as it used to be.\r\n\r\nExamples of automated detection\r\n\r\nmethods other than antivirus software are as follows:\r\n\r\n- Content Filtering. For example, email servers and clients, as well as anti-spam software, can be\r\nconfigured to block emails or email attachments that have certain characteristics, such as a known\r\nbad subject, sender, message text, or attachment name or type.19 This is only helpful when the\r\nmalware has static characteristics; highly customized malware usually cannot be blocked\r\neffectively using content filtering. Web content filtering and other content filtering technologies\r\nmay also be of use for static malware.\r\n\r\n- Network-Based IPS Software. Most IPS products allow their prevention capabilities to be\r\nenabled for specific signatures. If a network-based IPS device is inline, meaning that it is an\r\nactive part of the network, and it has a signature for the malware, it should be able to identify the\r\nmalware and stop it from reaching its targets. If the IPS device does not have its prevention\r\ncapabilities enabled, it may be prudent during a severe incident to reconfigure or redeploy one or\r\nmore IPS sensors and enable IPS so they can stop the activity. IPS technologies should be able to\r\nstop both incoming and outgoing infection attempts. Of course, the value of IPSs in malware\r\ncontainment depends on the availability and accuracy of a signature to identify the malware.\r\nSeveral IPS products allow administrators to write custom signatures based on some of the known\r\ncharacteristics of the malware, or to customize existing signatures. For example, an IPS may\r\nallow administrators to specify known bad email attachment names or subjects, or to specify\r\nknown bad destination port numbers. In many cases, IPS administrators can have their own\r\naccurate signature in place hours before antivirus vendors have signatures available. In addition,\r\nbecause the IPS signature affects only network-based IPS sensors, whereas antivirus signatures\r\ngenerally affect all workstations and servers, it is generally less risky to rapidly deploy a new IPS\r\nsignature than new antivirus signatures.\r\n\r\n- Executable Blacklisting. Some operating systems, host-based IPS products, and other\r\ntechnologies can restrict certain executables from being run. For example, administrators can\r\nenter the names of files that should not be executed. If antivirus signatures are not yet available\r\nfor a new threat, it might be possible to configure a blacklisting technology to block the execution\r\nof the files that are part of the new threat.\r\nContainment Through Disabling Services\r\n\r\nSome malware incidents necessitate more drastic and potentially disruptive measures for containment.\r\nThese incidents make extensive use of a particular service. Containing such an incident quickly and\r\neffectively might be accomplished through a loss of services, such as shutting down a service used by\r\nmalware, blocking a certain service at the network perimeter, or disabling portions of a service (e.g., large\r\nmailing lists). Also, a service might provide a channel for infection or for transferring data from infected\r\nhosts—for example, a botnet command and control channel using Internet Relay Chat (IRC). In either case, shutting down the affected services might be the best way to contain the infection without losing all\r\nservices. This action is typically performed at the application level (e.g., disabling a service on servers) or\r\nat the network level (e.g., configuring firewalls to block IP addresses or ports associated with a service).\r\nThe goal is to disable as little functionality as possible while containing the incident effectively. To\r\nsupport the disabling of network services, organizations should maintain lists of the services they use and\r\nthe TCP and UDP ports used by each service.\r\n\r\nContainment Through Disabling Connectivity\r\nContaining incidents by placing temporary restrictions on network connectivity can be very effective. For\r\nexample, if infected hosts attempt to establish connections with an external host to download rootkits,\r\nhandlers should consider blocking all access to the external host (by IP address or domain name, as\r\nappropriate). Similarly, if infected hosts within the organization attempt to spread their malware, the\r\norganization might block network traffic from the hosts’ IP addresses to control the situation while the\r\ninfected hosts are physically located and disinfected. An alternative to blocking network access for\r\nparticular IP addresses is to disconnect the infected hosts from the network, which could be accomplished\r\nby reconfiguring network devices to deny network access or physically disconnecting network cables\r\nfrom infected hosts.\r\n\r\nContainment Recommendations\r\n\r\nContainment can be performed through many methods in the four categories described above (users,\r\nautomated detection, loss of services, and loss of connectivity). Because no single malware containment\r\ncategory or individual method is appropriate or effective in every situation, incident handlers should\r\nselect a combination of containment methods that is likely to be effective in containing the current\r\nincident while limiting damage to hosts and reducing the impact that containment methods might have on\r\nother hosts. For example, shutting down all network access might be very effective at stopping the spread\r\nof malware, but it would also allow infections on hosts to continue damaging files and would disrupt\r\nmany important functions of the organization.");
                     
                        System.out.println("" +  MIR.getMIRC());    
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                        System.out.println();
                        System.out.println( "TO CONTINUE WITH NEXT MALWARE-INCIDENT-RESPONSE CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 6");
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                     
                     }
                     
                     else
                     
                        if ( menuSelect == 4)
                        
                        {
                           System.out.println();
                           System.out.println("MALWARE-INCIDENT-ERADICATION: ");
                           System.out.println();
                        
                           MIR.setMIRE("Eradication\r\n\r\nAlthough the primary goal of eradication is to remove malware from infected hosts, eradication is\r\ntypically more involved than that. If an infection was successful because of a host vulnerability or other\r\nsecurity weakness, such as an unsecured file share, then eradication includes the elimination or mitigation\r\nof that weakness, which should prevent the host from becoming reinfected or becoming infected by\r\nanother instance of malware or a variant of the original threat. Eradication actions are often consolidated\r\nwith containment efforts. For example, organizations might run a utility that identifies infected hosts,\r\napplies patches to remove vulnerabilities, and runs antivirus software that removes infections.\r\nContainment actions often limit eradication choices; for example, if an incident is contained by\r\ndisconnecting infected hosts from the primary network, the hosts should either be connected to a separate\r\nVLAN so that they can be updated remotely, or patched and reconfigured manually. Because the hosts are\r\ndisconnected from the primary network, the incident handlers will be under pressure to perform\r\neradication actions on the hosts as quickly as possible so that the users can regain full use of their hosts.\r\n\r\nOrganizations should be prepared to rebuild hosts quickly, as needed, when malware incidents occur.\r\nIn general, organizations should rebuild any host that has any of the following incident characteristics,\r\ninstead of performing typical eradication actions (disinfection):\r\n\r\n- One or more attackers gained administrator-level access to the host.\r\n\r\n- Unauthorized administrator-level access to the host was available to anyone through a backdoor,\r\nan unprotected share created by a worm, or other means.\r\n\r\n- System files were replaced by a Trojan horse, backdoor, rootkit, attacker tools, or other means.\r\n\r\n- The host is unstable or does not function properly after the malware has been eradicated by\r\nantivirus software or other programs or techniques. This indicates that either the malware has not\r\nbeen eradicated completely or that it has caused damage to important system or application files\r\nor settings.\r\n\r\n- There is doubt about the nature of and extent of the infection or any unauthorized access gained\r\nbecause of the infection.\r\n\r\nIf a malware incident does not have any of these characteristics, then it is typically sufficient to eradicate\r\nthe malware from the host instead of rebuilding the host.\r\n\r\nEradication can be frustrating because of the number of hosts to clean up and the tendency to have\r\nadditional infections and reinfections occurring for days, weeks, or months.20 Incident handlers should\r\nperiodically perform identification activities to identify hosts that are still infected and estimate the success of the eradication. A reduction in the number of infected hosts would demonstrate that the\r\nincident response team was making progress and would help the team choose the best strategy for\r\nhandling the remaining hosts and allocate sufficient time and resources. It can be tempting to declare an\r\nincident resolved once the number of infected hosts has dropped significantly from the original numbers,\r\nbut the organization should strive to reduce the suspected numbers of infected and vulnerable machines to\r\nlow enough levels that if they were all connected to the network at once and the vulnerable machines all\r\nbecame infected, the overall impact of the infections would be minimal.");
                        
                           System.out.println("" + MIR.getMIRE());      
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                           System.out.println();
                           System.out.println( "TO CONTINUE WITH NEXT MALWARE-INCIDENT-RESPONSE CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 6");
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                        
                        }
                        
                        else
                        
                           if ( menuSelect == 5)
                           
                           {
                              System.out.println();         
                              System.out.println();
                              System.out.println("MALWARE-INCIDENT-RECOVERY:"); 
                              System.out.println();     
                           
                           
                              MIR.setMIRR("Recovery\r\nThe two main aspects of recovery from malware incidents are restoring the functionality and data of\r\ninfected hosts and removing temporary containment measures. Additional actions to restore hosts are not\r\nnecessary for most malware incidents that cause limited host damage (for example, an infection that\r\nsimply altered a few data files and was completely removable with antivirus software).\r\nFor malware incidents that are far more damaging, such as Trojan horses, rootkits, or\r\nbackdoors, corrupting thousands of system and data files, or wiping out hard drives, it is often best to first\r\nrebuild the host, then secure the host so that it is no longer vulnerable to the malware threat.\r\nOrganizations should carefully consider possible worst-case scenarios, such as a new malware threat that\r\nnecessitates rebuilding a large percentage of the organization’s workstations, and determine how the hosts\r\nwould be recovered in these cases. This should include identifying who would perform the recovery tasks,\r\nestimating how many hours of labor would be needed and how much calendar time would elapse, and\r\ndetermining how the recovery efforts should be prioritized. ");
                           
                           
                              System.out.println("" + MIR.getMIRR());
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                              System.out.println();
                              System.out.println( "TO CONTINUE WITH NEXT MALWARE-INCIDENT-RESPONSE CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 6");
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                           
                           }
                           
                           else
                           
                              if ( menuSelect == 6)
                              
                              {
                                 System.out.println();         
                                 System.out.println();
                                 System.out.println("MALWARE-INCIDENT-LESSONS-LEARNED: "); 
                                 System.out.println();     
                              
                              
                                 MIR.setMILL("Lessons Learned\r\nWhen a major malware incident occurs, the primary individuals performing the response usually work\r\nintensively for days or weeks. As the major handling efforts end, the key people are usually mentally and\r\nphysically fatigued, and are behind in performing other tasks that were pending during the incident\r\nhandling period. Consequently, the lessons learned phase of incident response might be significantly\r\ndelayed or skipped altogether for major malware incidents. However, because major malware incidents\r\ncan be extremely expensive to handle, it is particularly important for organizations to conduct robust\r\nlessons learned activities for major malware incidents. Although it is reasonable to give handlers and\r\nother key people a few days to catch up on other tasks, review meetings and other efforts should occur\r\nexpeditiously, while the incident is still fresh in everyone’s minds. The lessons learned process for\r\nmalware incidents is no different than for any other type of incident. Examples of possible outcomes of\r\nlessons learned activities for malware incidents are as follows:\r\n\r\n1. Security Policy Changes. Security policies might be modified to prevent similar incidents. For\r\nexample, if connecting personally owned mobile devices to organization laptops caused a serious\r\ninfection, modifying the organization’s policies to secure, restrict, or prohibit such device\r\nconnections might be advisable.\r\n\r\n2. Awareness Program Changes. Security awareness training for users might be changed to reduce\r\nthe number of infections or to improve users’ actions in reporting incidents and assisting with\r\nhandling incidents on their own hosts.\r\n\r\n3. Software Reconfiguration. OS or application settings might need to be changed to support\r\nsecurity policy changes or to achieve compliance with existing policy.\r\n\r\n4. Malware Detection Software Deployment. If hosts were infected through a transmission\r\nmechanism that was unprotected by antivirus software or other malware detection tools, an\r\nincident might provide sufficient justification to purchase and deploy additional software.\r\n\r\n4. Malware Detection Software Reconfiguration. Detection software might need to be\r\nreconfigured in various ways, such as the following:\r\n\r\n– Increasing the frequency of software and signature updates\r\n\r\n– Improving the accuracy of detection (e.g., fewer false positives, fewer false negatives)\r\n\r\n– Increasing the scope of monitoring (e.g., monitoring additional transmission mechanisms,\r\nmonitoring additional files or file systems)\r\n\r\n– Changing the action automatically performed in response to detected malware\r\n\r\n– Improving the efficiency of update distribution. ");
                              
                              
                                 System.out.println("" + MIR.getMILL());
                                 System.out.println();
                                 System.out.println("************************************************************************************************" );
                                 System.out.println();
                                 System.out.println( "TO CONTINUE WITH NEXT MALWARE-INCIDENT CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                                 System.out.println();
                                 System.out.println("************************************************************************************************" );
                              
                              }
                              
                              
                              else
                              
                                 System.out.println();
               System.out.println   ("HERE ARE EMAIL-ISOLATION-FRAMEWORK MAIN MENU CATEGORIES LIST: ");
               System.out.println();
               System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
               System.out.println();
               System.out.println   ("2.  EMAIL STANDARDS ."); 
               System.out.println();
               System.out.println   ("3.  EMAIL SECURITY THREATS."); 
               System.out.println();
               System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
               System.out.println();
               System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
               System.out.println();
               System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
               System.out.println();
               System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
               System.out.println();
               System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
               System.out.println();
               System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
               System.out.println();
               System.out.println   ("12. SECURING EMAIL CLIENTS."); 
               System.out.println();
               System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
               System.out.println();
               System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
               System.out.println();
               System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
            
               menuSelection = keyboard.nextInt();
            
               while (menuSelection < 1 || menuSelection > 17) 
               
               {
               
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();  
                  System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("HERE IS THE VALID LIST OF EMAIL-ISOLATION MAIN MENU CATEGORIES: ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
                  System.out.println();
                  System.out.println   ("2.  EMAIL STANDARDS ."); 
                  System.out.println();
                  System.out.println   ("3.  EMAIL SECURITY THREATS."); 
                  System.out.println();
                  System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
                  System.out.println();
                  System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
                  System.out.println();
                  System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
                  System.out.println();
                  System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
                  System.out.println();
                  System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
                  System.out.println();
                  System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
                  System.out.println();
                  System.out.println   ("12. SECURING EMAIL CLIENTS."); 
                  System.out.println();
                  System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
                  System.out.println();
                  System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
                  System.out.println();
                  System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
               
               
               
                  menuSelection = keyboard.nextInt();
               
               } 
            
               break;
         
            case 7:
            
               EmailIsolationSetter SEEM;
               SEEM = new EmailIsolationSetter();
            
            
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println("YOU SELECTED SIGNING-&-ENCRYPTING-EMAIL-MESSAGES CATEGORY FROM EMAIL-ISOLATION MAIN MENU ");
               System.out.println();
               System.out.println("PLEASE SEE BELOW SIGNING-&-ENCRYPTING-EMAIL-MESSAGES  SUBCATEGORIES: ");
               System.out.println(); 
               System.out.println("1.  OpenPGP.");
               System.out.println();
               System.out.println("2.  S/MIME.");
               System.out.println();
               System.out.println("3.  KEY MANAGEMENT.");
               System.out.println();
               System.out.println("4.  ISSUES WITH EMAIL ENCRYPTION.");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print(" ENTER YOUR SIGNING-&-ENCRYPTING-EMAIL-MESSAGES CHOICE (1 to 4): ");
            
            
               menuSelect = keyboard.nextInt();
            
               while (menuSelect < 1 || menuSelect > 4)
               
               {
               
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println("THIS IS INVALID CHOICE FOR SIGNING-&-ENCRYPTING-EMAIL-MESSAGES SELECTION "); 
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW VALID SIGNING-&-ENCRYPTING-EMAIL-MESSAGES SELECTIONS:");
                  System.out.println();
                  System.out.println("1.  OpenPGP.");
                  System.out.println();
                  System.out.println("2.  S/MIME.");
                  System.out.println();
                  System.out.println("3.  KEY MANAGEMENT.");
                  System.out.println();
                  System.out.println("4.  ISSUES WITH EMAIL ENCRYPTION.");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER YOUR SIGNING-&-ENCRYPTING-EMAIL-MESSAGES CHOICE (1 to 4): ");
               
               
               
                  menuSelect = keyboard.nextInt();
               
               }
            
            //System.out.println();
            //System.out.println("Organizations often want to protect the confidentiality and integrity of some of their email messages, such/r/nas preventing the exposure of personally identifiable information in an email attachment. Email messages/r/ncan be protected by using cryptography in various ways, such as the following:/r/n/r/nSign an email message to ensure its integrity and confirm the identity of its sender./r/n/r/n- Encrypt the body of an email message to ensure its confidentiality./r/n/r/n- Encrypt the communications between mail servers to protect the confidentiality of both the message/r/nbody and message header./r/n/r/nThe first two methods, message signing and message body encryption, are often used together. For/r/nexample, if a message needs to be encrypted to protect its confidentiality, it is usually digitally signed as/r/nwell, so that the recipient can ensure the integrity of the message and verify the identity of the signer./r/nMessages that are digitally signed are usually not encrypted if the confidentiality of the contents does not/r/nneed to be protected. ".toUpperCase());
            //System.out.println();                
            //System.out.println(" NOTE:  Without all eight of these currencies, you don’t have a true EMAIL-ISOLATION network. With them, you have a powerful, game-changing platform for innovation .".toUpperCase());
            // System.out.println(); 
            
               if ( menuSelect == 1)
               
               {          
                  System.out.println();
                  System.out.println("OPENPGP-SELECTION: ");
                  System.out.println();
               
               
                  SEEM.setPGP           ("Organizations often want to protect the confidentiality and integrity of some of their email messages, such/r/nas preventing the exposure of personally identifiable information in an email attachment. Email messages/r/ncan be protected by using cryptography in various ways, such as the following:/r/n/r/nSign an email message to ensure its integrity and confirm the identity of its sender./r/n/r/n- Encrypt the body of an email message to ensure its confidentiality./r/n/r/n- Encrypt the communications between mail servers to protect the confidentiality of both the message/r/nbody and message header./r/n/r/nThe first two methods, message signing and message body encryption, are often used together. For/r/nexample, if a message needs to be encrypted to protect its confidentiality, it is usually digitally signed as/r/nwell, so that the recipient can ensure the integrity of the message and verify the identity of the signer./r/nMessages that are digitally signed are usually not encrypted if the confidentiality of the contents does not/r/nneed to be protected.\r\n\r\nOpenPGP\r\n\r\nOpenPGP is a protocol for encrypting and signing messages and for creating certificates using public key\r\ncryptography. It is based on an earlier protocol, PGP, which was created by Phil Zimmerman and\r\nimplemented as a product first released in June 1991. The initial PGP protocol was proprietary and used\r\nsome encryption algorithms with intellectual property restrictions.\r\n\r\nMany free and commercial products that use the OpenPGP standard are currently available. The software\r\ncan be downloaded or purchased from a variety of Web sites.15 Some OpenPGP-based products fully\r\nsupport the cryptographic algorithms recommended to the Federal government by NIST in FIPS PUB\r\n140-2 and other publications, including 3DES and AES for data encryption, Digital Signature Algorithm\r\n(DSA and RSA for digital signatures, and SHA for hashing. Some implementations of OpenPGP\r\nsupport other encryption schemes not addressed here.\r\n\r\nAlthough certain aspects of OpenPGP do use public key cryptography, such as digitally signed message\r\ndigests, the actual encryption of the message body is performed with a symmetric key algorithm, as\r\noutlined earlier. The following is a brief description of signing and encrypting a message with OpenPGP\r\n(some steps may occur in a different order):\r\n\r\n- OpenPGP compresses the plaintext, which reduces transmission time and strengthens cryptographic\r\nsecurity by obfuscating plaintext patterns commonly searched for during cryptanalysis.\r\n\r\n- OpenPGP creates a random session key (in some implementations of OpenPGP, users are required to\r\nmove their mouse at will within a window to generate random data).\r\n\r\n- A digital signature is generated for the message using the sender’s private key, and then added to the message.\r\n\r\n- The message and signature are encrypted using the session key and a symmetric algorithm (e.g.,3DES, AES).\r\n\r\n- The session key is encrypted using the recipient’s public key and added to the beginning of the encrypted message.\r\n\r\n- The encrypted message is sent to the recipient.\r\n\r\nThe recipient reverses the steps to recover the session key, decrypt the message, and verify the signature.\r\nPopular mail clients such as Mozilla Thunderbird, Apple Mail, Eudora, and Microsoft Outlook require the\r\ninstallation of plug-ins to enable the user to send and receive OpenPGP-encrypted messages. The\r\nOpenPGP distribution sites listed earlier in this section contain instructions on how to use OpenPGP with\r\nvarious mail client applications. ");
               
               
                  System.out.println               ("" +  SEEM.getPGP());
                  System.out.println();          
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println( "TO CONTINUE WITH NEXT SIGNING-&-ENCRYPTING-EMAIL-MESSAGES CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU  CHOICE # 7");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
               
               }
               
               else
               
                  if ( menuSelect == 2)
                  
                  {
                     System.out.println();
                     System.out.println();
                     System.out.println("S/MIME-SELECTION: ");
                     System.out.println();
                  
                     SEEM.setSMIME ("S/MIME\r\n\r\nS/MIME, which was originally proposed in 1995 by RSA Data Security, Inc., is based on their\r\nproprietary (although widely supported) Public Key Cryptography Standard (PKCS) #7 for data format of\r\nencrypted messages, and the X.509 version 3 standard for digital certificates.18 S/MIME version 2\r\nachieved wide adoption throughout the Internet mail industry.\r\n\r\nS/MIME version 3 was developed by the IETF S/MIME Working Group, which now coordinates all\r\ndevelopment of the S/MIME standard,19 and adopted as an IETF standard in July 1999. S/MIME version\r\n3 is specified by the following RFCs:\r\n\r\n- Cryptographic Message Syntax (RFC 3852)\r\n\r\n- S/MIME Version 3 Message Specification (RFC 3851)\r\n\r\n-  S/MIME Version 3 Certificate Handling (RFC 3850)\r\n\r\n- Diffie-Hellman Key Agreement Method (RFC 2631)\r\n\r\n- Enhanced Security Services for S/MIME (RFC 2634).\r\n\r\nThe most significant feature of S/MIME is its built-in and nearly “automatic” nature. Because of heavy\r\nindustry involvement from manufacturers, S/MIME functionality exists with default installations of\r\ncommon mail clients such as Mozilla and Outlook Express.\r\n\r\nThe actual process by which S/MIME-enabled mail clients send messages is similar to that of\r\nOpenPGP S/MIME version 3.1 supports two symmetric key encryption algorithms recommended by\r\nFIPS PUB 140-2: AES, which is recommended but optional for compliant implementations to support,\r\nand 3DES, which is mandatory for implementations to support. Organizations using S/MIME to protect\r\nemails should use AES or 3DES (preferably AES, which is considered a stronger algorithm than 3DES).\r\n\r\nAs with OpenPGP, there are security gateway servers available that can use S/MIME to encrypt, decrypt,\r\nsign, and verify signatures on email messages on behalf of users. These gateways are very similar to\r\nthose described in Section 3.1, and many of the gateways actually support both OpenPGP and S/MIME.");
                  
                  
                  
                     System.out.println("" +  SEEM.getSMIME());
                     System.out.println();
                     System.out.println("************************************************************************************************" );
                     System.out.println();
                     System.out.println( "TO CONTINUE WITH NEXT SIGNING-&-ENCRYPTING-EMAIL-MESSAGES CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 7");
                     System.out.println();
                     System.out.println("************************************************************************************************" );   
                  
                  }
                  
                  else
                  
                     if ( menuSelect == 3 )
                     
                     {
                        System.out.println();
                        System.out.println();
                        System.out.println("KEY-MANAGEMENT: ");
                        System.out.println();  
                     
                        SEEM.setKM("Both OpenPGP and S/MIME use digital certificates to manage keys. A digital certificate identifies the\r\nentity (e.g., a user) that was issued the certificate, the public key of the entity’s public key pair, and other\r\ninformation, such as the date of expiration, signed by some trusted party. However, differences exist in\r\nthe key management models used by OpenPGP and S/MIME to establish trust using digital certificates.\r\n\r\nThe default and traditional model that OpenPGP uses for key management is referred to as the “web of\r\ntrust,” which has no central key issuing or approving authority. The web of trust relies on the personal\r\ndecisions of users for management and control. For example, if Alice trusts Bob and Carol trusts Alice,\r\nthen Carol should trust Bob’s emails. While this is suitable for individual users and very small\r\norganizations, the overhead of such a system is unworkable in most medium to large organizations. Some\r\norganizations deploy keyservers that users can access to get others’ keys and store their own keys.\r\nAlthough this does promote scalability, the process is typically controlled mainly by individual users, and\r\norganizations are often not comfortable trusting keyservers to provide sufficient assurance of user identity.\r\n\r\nConversely, S/MIME works on a classical, more hierarchical arrangement of authorities that the\r\norganization chooses to trust. Typically, there is a master registration and approving authority, referred to\r\nas a root Certificate Authority (CA), that issues a public key certificate for itself and any subordinate CAs\r\nit sanctions. Subordinate CAs normally issue certificates to users and also to any other subordinate CAs\r\nthat they in turn sanction, forming a hierarchy. Such a public key infrastructure can be used to establish a\r\nchain of trust between any two users holding valid certificates issued under it. By default, S/MIMEenabled mail clients depend on the trust of their immediate master CA when processing S/MIME\r\ntransactions. This authority can be either a third-party CA21 or a CA that is controlled by the organization\r\nissuing the certificates.\r\n\r\nWork is currently underway on a possible method of reducing key management concerns for email\r\nsigning and encryption. Identity-based encryption (IBE) is a form of public key encryption that allows\r\nany string to be used as a public key. By using email addresses as public keys, IBE could simplify key\r\nmanagement, making it much easier for senders to protect the emails that they send. However, there are\r\nserious barriers to adoption of IBE, including no open standards for IBE and no FIPS-approved IBE\r\nproducts. Informational Internet-Drafts have been started that propose how IBE could be performed\r\nusing S/MIME.");
                     
                        System.out.println("" +  SEEM.getKM());    
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                        System.out.println();
                        System.out.println( "TO CONTINUE WITH NEXT SIGNING-&-ENCRYPTING-EMAIL-MESSAGES CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 7");
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                     
                     }
                     
                     else
                     
                        if ( menuSelect == 4)
                        
                        {
                           System.out.println();
                           System.out.println("ISSUES WITH EMAIL-ENCRYPTION: ");
                           System.out.println();
                        
                           SEEM.setISSUE("Issues with Email Encryption\r\n\r\nAlthough encrypting email provides additional security, it does come at a cost, so organizations should\r\ncarefully weigh the issues associated with encrypting email messages:\r\n\r\n- Scanning for viruses and other malware and filtering email content at the firewall and mail server isr\r\nmade significantly more complicated by encryption. If the firewall or mail server does not have a\r\nmethod for decrypting the email, it cannot read and act upon the contents. Some malware scanners\r\ncan decrypt emails if the scanner is a recipient of the emails or if the sender specifically encrypts the\r\nemails for the scanner, but such solutions are technically complex and often hard to enforce. Also,\r\ngiving the malware scanner the ability to decrypt many or all emails could have serious consequences\r\nif the malware scanner host is itself infected or otherwise compromised. If having the malware\r\nscanner decrypt emails is not feasible, scanning might have to be performed on the hosts of the mail\r\nclients that perform decryption.\r\n\r\n- Encryption and decryption require processor time. Organizations might need to upgrade or replace\r\nequipment that is not capable of supporting the load of encryption and decryption\r\n\r\n- Organization-wide use of encryption can require significant ongoing administrative overhead.\r\nExamples of this include key distribution, key recovery, and revocation of encryption keys.\r\n\r\n- Email encryption can complicate the review of email messages by law enforcement and other\r\ninvestigative parties.\r\n- Encrypted emails sent to or received from other organizations may be insufficiently protected if those\r\norganizations do not support the use of strong encryption algorithms and key sizes. Organizations\r\nshould ensure that their users’ mail applications notify them when they receive a weakly encrypted\r\nmessage or when they are attempting to send an encrypted message to a recipient that only supports\r\nweak encryption methods. Users can then contact the relevant party to notify them of the problem\r\nand request that they either use a stronger encryption algorithm or transfer the information that needs\r\nprotected through a mechanism other than email. ");
                        
                           System.out.println("" + SEEM.getISSUE());      
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                           System.out.println();
                           System.out.println( "TO CONTINUE WITH NEXT SIGNING-&-ENCRYPTING-EMAIL-MESSAGES CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 7");
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                        
                        }
                        
                        else
                        
                           System.out.println();
               System.out.println   ("HERE ARE EMAIL-ISOLATION-FRAMEWORK MAIN MENU CATEGORIES LIST: ");
               System.out.println();
               System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
               System.out.println();
               System.out.println   ("2.  EMAIL STANDARDS ."); 
               System.out.println();
               System.out.println   ("3.  EMAIL SECURITY THREATS."); 
               System.out.println();
               System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
               System.out.println();
               System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
               System.out.println();
               System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
               System.out.println();
               System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
               System.out.println();
               System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
               System.out.println();
               System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
               System.out.println();
               System.out.println   ("12. SECURING EMAIL CLIENTS."); 
               System.out.println();
               System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
               System.out.println();
               System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
               System.out.println();
               System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
            
               menuSelection = keyboard.nextInt();
            
               while (menuSelection < 1 || menuSelection > 17) 
               
               {
               
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();  
                  System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("HERE IS THE VALID LIST OF EMAIL-ISOLATION MAIN MENU CATEGORIES: ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
                  System.out.println();
                  System.out.println   ("2.  EMAIL STANDARDS ."); 
                  System.out.println();
                  System.out.println   ("3.  EMAIL SECURITY THREATS."); 
                  System.out.println();
                  System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
                  System.out.println();
                  System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
                  System.out.println();
                  System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
                  System.out.println();
                  System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
                  System.out.println();
                  System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
                  System.out.println();
                  System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
                  System.out.println();
                  System.out.println   ("12. SECURING EMAIL CLIENTS."); 
                  System.out.println();
                  System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
                  System.out.println();
                  System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
                  System.out.println();
                  System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
               
               
               
                  menuSelection = keyboard.nextInt();
               
               } 
            
               break;
         
            case 8:
            
               EmailIsolationSetter PMS;
               PMS = new EmailIsolationSetter();
            
            
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println("YOU SELECTED PLANNING-&-MANAGING-EMAIL-SERVERS CATEGORY FROM EMAIL-ISOLATION MAIN MENU ");
               System.out.println();
               System.out.println("PLEASE SEE BELOW PLANNING-&-MANAGING-EMAIL-SERVERS SUBCATEGORIES: ");
               System.out.println(); 
               System.out.println("1.  INSTALLATION AND DEPLOYMENT PLANNING.");
               System.out.println();
               System.out.println("2.  SECURITY MANAGEMENT STAFF.");
               System.out.println();
               System.out.println("3.  MANAGEMENT PRACTICES.");
               System.out.println();
               System.out.println("4.  SYSTEM SECURITY PLAN.");
               System.out.println();
               System.out.println("5.  HUMAN RESOURCES REQUIREMENTS.");
               System.out.println();
               System.out.println("6.  GENERAL INFORMATION SYSTEM SECURITY PRINCIPLES.");
               System.out.println();
               System.out.println("7.  CHECKLIST FOR PLANNING AND MANAGING SERVERS.");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER YOUR PLANNING-&-MANAGING-EMAIL-SERVERS CHOICE (1 to 7): ");
            
            
               menuSelect = keyboard.nextInt();
            
               while (menuSelect < 1 || menuSelect > 7)
               
               {
               
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println("THIS IS INVALID CHOICE PLANNING-&-MANAGING-EMAIL-SERVERS SELECTION "); 
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW VALID PLANNING-&-MANAGING-EMAIL-SERVERS SELECTIONS:");
                  System.out.println();
                  System.out.println("1.  INSTALLATION AND DEPLOYMENT PLANNING.");
                  System.out.println();
                  System.out.println("2.  SECURITY MANAGEMENT STAFF.");
                  System.out.println();
                  System.out.println("3.  MANAGEMENT PRACTICES.");
                  System.out.println();
                  System.out.println("4.  SYSTEM SECURITY PLAN.");
                  System.out.println();
                  System.out.println("5.  HUMAN RESOURCES REQUIREMENTS.");
                  System.out.println();
                  System.out.println("6.  GENERAL INFORMATION SYSTEM SECURITY PRINCIPLES.");
                  System.out.println();
                  System.out.println("7.  CHECKLIST FOR PLANNING AND MANAGING SERVERS.");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print(" ENTER YOUR PLANNING-&-MANAGING-EMAIL-SERVERS CHOICE (1 to 7): ");
               
               
               
               
                  menuSelect = keyboard.nextInt();
               
               }
            
            //System.out.println();
            //System.out.println(" NOTE: There are eight performance attributes, or currencies, to be considered when evaluating whether a EMAIL-ISOLATION network can deliver on its full potential.".toUpperCase());
            //System.out.println();                
            //System.out.println(" NOTE:  Without all eight of these currencies, you don’t have a true EMAIL-ISOLATION network. With them, you have a powerful, game-changing platform for innovation .".toUpperCase());
            //System.out.println(); 
            
               if ( menuSelect == 1)
               
               {          
                  System.out.println();
                  System.out.println("INSTALLATION-AND-DEPLOYMENT-PLANNING: ");
                  System.out.println();
               
               
                  PMS.setIDP           ("Installation and Deployment Planning\r\nSecurity of the mail server should be considered from the initial planning stage at the beginning of the\r\nsystems development life cycle to maximize security and minimize costs. It is much more difficult and\r\nexpensive to address security once implementation and deployment have occurred. Organizations are\r\nmore likely to make decisions about configuring hosts appropriately and consistently when they begin by\r\ndeveloping and using a detailed, well-designed deployment plan. Developing such a plan enables\r\norganizations to make informed tradeoff decisions between usability and performance, and risk.\r\n A deployment plan allows organizations to maintain secure configurations and aids in identifying security\r\nvulnerabilities, which often manifest themselves as deviations from the plan.\r\n\r\nIn the planning stages of a mail server, the following items should be considered:\r\n\r\n1. Identify the purpose(s) of the mail server.\r\n\r\n– What information categories will be stored on, processed on, or transmitted through the mail\r\nserver?\r\n\r\n– What are the security requirements for this information?\r\n\r\n– What other service(s) will be provided by the mail server (in general, dedicating the host to being\r\nonly a mail server is the most secure option)?\r\n\r\n– What are the security requirements for these additional services?\r\n\r\n– What are the requirements for continuity of mail services, such as those specified in continuity of\r\noperations plans and disaster recovery plans?\r\n\r\n– Where on the network will the mail server be located?\r\n\r\n2. Identify the network services that will be provided on the mail server (in addition to the organization’s standard services provided by every server for backup, remote administration, etc.),\r\nsuch as those supplied through standard email protocols (e.g., SMTP, POP, IMAP) and proprietary email protocols.\r\n\r\n3. Identify any network service software, both client and server, to be installed on the mail server and\r\nany other support servers.\r\n\r\n3. Identify the users or categories of users of the mail server and any support hosts, including servers\r\nproviding Web-based mail access.\r\n\r\n4. Determine the privileges that each category of user will have on the mail server and support hosts.\r\n\r\n5. Determine how the mail server will be managed (e.g., locally, remotely from the internal network,\r\nremotely from external networks).\r\n\r\n6. Decide if and how users will be authenticated and how authentication data will be protected.\r\n\r\n7. Identify any security or privacy requirements for address-related information, such as username, user\r\nidentity, and organizational association.\r\n\r\n8. Determine how appropriate access to information resources will be enforced.\r\n\r\n9. Determine which mail server applications meet the organization’s requirements. Consider servers\r\nthat may offer greater security, albeit with less functionality in some instances. Some issues to\r\nconsider include the following:\r\n\r\n– Cost\r\n\r\n– Compatibility with existing infrastructure\r\n\r\n– Knowledge of existing employees\r\n\r\n– Existing manufacturer relationship\r\n\r\n– Past vulnerability history\r\n\r\n– Functionality\r\n\r\n10. Work closely with manufacturer(s) in the planning stage.\r\n\r\nThe choice of mail server application may determine the choice of operating system. However, to the\r\ndegree possible, mail server administrators should choose an operating system that provides the following\r\n\r\n:11. Minimal exposure to vulnerabilities (which can be identified on all operating systems)\r\n\r\n12. Ability to restrict administrative or root level activities to authorized users only\r\n\r\n13. Ability to deny access to information on the server other than that intended to be available\r\n\r\n14. Ability to disable unnecessary network services that may be built into the operating system or server software\r\n\r\n15. Ability to log appropriate server activities to detect intrusions and attempted intrusions.\r\n\r\nIn addition, organizations should consider the availability of trained, experienced staff to administer the\r\nserver and server products. Many organizations have learned the difficult lesson that a capable and\r\nexperienced administrator for one type of operating environment is not automatically as effective for another.\r\n\r\nGiven the sensitive nature of the mail server, it is critical that it is located in an area that provides a secure\r\nphysical environment. When planning the location of the mail server, the following items should be considered:\r\n\r\n15.  Does the proposed location offer the appropriate physical security protection mechanisms? Examples\r\ninclude locks, card reader access, security guards, and physical intrusion detection systems (e.g.,\r\nmotion sensors, cameras).\r\n\r\n16. Does the proposed location offer the appropriate environmental controls so that the necessary\r\nhumidity and temperature are maintained?\r\n\r\n17. Is there a backup power source?\r\n\r\n18. If the location is subject to known natural disasters, is it hardened against those disasters and/or is\r\nthere a contingency site outside the potential disaster area?");
               
               
                  System.out.println       ("" +  PMS.getIDP());
                  System.out.println();          
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println( "TO CONTINUE WITH NEXT PLANNING-&-MANAGING-EMAIL-SERVERS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU  CHOICE # 8");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
               
               }
               
               else
               
                  if ( menuSelect == 2)
                  
                  {
                     System.out.println();
                     System.out.println();
                     System.out.println("SECURITY-MANAGEMENT-STAFF: ");
                     System.out.println();
                  
                     PMS.setSMS ("Senior IT Management/Chief Information Officer (CIO)\r\n\r\nThe Senior IT Management/CIO ensures that the organization’s security posture is adequate. The Senior\r\nIT Management provides direction and advisory services for the protection of information systems for the\r\nentire organization. The Senior IT Management/CIO is responsible for the following activities that are\r\nassociated with mail servers:\r\n\r\n- Coordinating the development and maintenance of the organization’s information security policies,\r\nstandards, and procedures\r\n\r\n- Coordinating the development and maintenance of the organization’s change control and management\r\nprocedures\r\n\r\n- Ensuring the establishment of, and compliance with, consistent IT security policies for departments\r\nthroughout the organization\r\n\r\n- Coordinating with upper management, public affairs, and other relevant personnel to produce a\r\nformal policy and process for email usage guidelines (e.g., personal use, monitoring, encryption).\r\n\r\nInformation Systems Security Program Managers\r\n\r\nThe Information Systems Security Program Managers (ISSPM) oversee the implementation of and\r\ncompliance with the standards, rules, and regulations specified in the organization’s security policy. The\r\nISSPMs are responsible for the following activities associated with mail servers:\r\n\r\n- Ensuring that security procedures are developed and implemented\r\n\r\n- Ensuring that security policies, standards, and requirements are followed\r\n\r\n- Ensuring that all critical systems are identified and that contingency planning, disaster recovery plans,\r\nand continuity of operations plans exist for these critical systems\r\n\r\n-Ensuring that critical systems are identified and scheduled for periodic security testing according to\r\nthe security policy requirements of each respective system.\r\n\r\nInformation Systems Security Officers\r\n\r\nInformation Systems Security Officers (ISSO) are responsible for overseeing all aspects of information\r\nsecurity within a specific organizational entity. They ensure that the organization’s information security\r\npractices comply with organizational and departmental policies, standards, and procedures. ISSOs are\r\nresponsible for the following activities associated with mail servers:\r\n\r\n- Developing internal security standards and procedures for the mail server(s) and supporting network infrastructure\r\n\r\n- Cooperating in the development and implementation of security tools, mechanisms, and mitigation techniques\r\n\r\n- Maintaining standard configuration profiles of the mail servers and supporting network infrastructure\r\ncontrolled by the organization, including but not limited to operating systems, firewalls, routers, and\r\nmail server applications\r\n\r\n- Maintaining operational integrity of systems by conducting security tests and ensuring that designated\r\nIT professionals are conducting scheduled testing on critical systems.\r\n\r\nMail Server and Network Administrators\r\n\r\nMail server administrators are system architects responsible for the overall design, implementation, and\r\nmaintenance of a mail server. Network administrators are responsible for the overall design,\r\nimplementation, and maintenance of a network. On a daily basis, mail server and network administrators\r\ncontend with the security requirements of the specific system(s) for which they are responsible. Security\r\nissues and solutions can originate from either outside (e.g., security patches and fixes from the\r\nmanufacturer or computer security incident response teams) or within the organization (e.g., the security office). \r\nThe administrators are responsible for the following activities associated with mail servers:\r\n\r\n- Installing and configuring hosts in compliance with the organizational security policies and standard\r\nsystem/network configurations\r\n\r\n- Maintaining hosts in a secure manner, including frequent backups and timely application of patches\r\n- Monitoring system integrity, protection levels, and security-related events\r\n\r\n- Following up on detected security anomalies associated with their information system resources\r\n\r\n- Conducting security tests as required. ");
                  
                  
                  
                     System.out.println("" +  PMS.getSMS());
                     System.out.println();
                     System.out.println("************************************************************************************************" );
                     System.out.println();
                     System.out.println( "TO CONTINUE WITH NEXT PLANNING-&-MANAGING-EMAIL-SERVERS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 8");
                     System.out.println();
                     System.out.println("************************************************************************************************" );   
                  
                  }
                  
                  else
                  
                     if ( menuSelect == 3 )
                     
                     {
                        System.out.println();
                        System.out.println();
                        System.out.println("MANAGEMENT-PRACTICES: ");
                        System.out.println();  
                     
                        PMS.setMP("Management Practices\r\n\r\nAppropriate management practices are critical to operating and maintaining a secure mail server.\r\nSecurity practices entail the identification of an organization’s information system assets and the\r\ndevelopment, documentation, and implementation of policies, standards, procedures, and guidelines that\r\nensure confidentiality, integrity, and availability of information system resources.\r\n\r\nTo ensure the security of a mail server and the supporting network infrastructure, organizations should\r\nimplement the following practices:\r\n\r\n- Organizational Information System Security Policy—A security policy should specify the basic\r\ninformation system security tenets and rules and their intended internal purpose. The policy should\r\nalso outline who in the organization is responsible for particular areas of information security (e.g.,\r\nimplementation, enforcement, audit, review). The policy must be enforced consistently throughout\r\nthe organization to be effective. Generally, the CIO and upper management are responsible for\r\ndrafting the organization’s security policy.\r\n\r\n- Configuration/Change Control and Management—The process of controlling modification to a\r\nsystem’s design, hardware, firmware, and software provides sufficient assurance that the system is\r\nprotected against the introduction of an improper modification before, during, and after system\r\nimplementation. Configuration control leads to consistency with the organization’s information\r\nsystem security policy. Configuration control is traditionally overseen by a configuration control\r\nboard that is the final authority on all proposed changes to an information system.\r\n\r\n- Risk Assessment and Management—Risk assessment is the process of analyzing and interpreting\r\nrisk. It involves determining an assessment’s scope and methodology, collecting and analyzing riskrelated data, and interpreting the risk analysis results. Collecting and analyzing risk data requires\r\nidentifying assets, threats, vulnerabilities, safeguards, consequences, and the probability of a\r\nsuccessful attack. Risk management is the process of selecting and implementing controls to reduce\r\nrisk to a level acceptable to the organization.\r\n\r\n- Standardized Configurations—Organizations should develop standardized secure configurations\r\nfor widely used operating systems and applications. This will provide guidance to mail server and\r\nnetwork administrators on how to configure their systems securely and ensure consistency and\r\ncompliance with the organizational security policy. Because it only takes one insecurely configured\r\nhost to compromise a network, organizations with a significant number of hosts are especially\r\nencouraged to apply this recommendation. Section 5 contains additional information on standard\r\nconfigurations.\r\n\r\n- Security Awareness and Training—A security training program is critical to the overall security\r\nposture of an organization. Making users and administrators aware of their security responsibilities\r\nand teaching the correct practices helps them change their behavior to conform to security best\r\npractices. Training also supports individual accountability, which is an important method for\r\nimproving information system security.\r\n\r\n- Contingency, Continuity of Operations, and Disaster Recovery Planning—Contingency plans,\r\ncontinuity of operations plans, and disaster recovery plans are established in advance to allow an\r\norganization or facility to maintain operations in the event of a disruption.\r\n\r\n- Certification and Accreditation—Certification in the context of information systems security means\r\nthat a system has been analyzed as to how well it meets all of the security requirements of the\r\norganization. Accreditation occurs when the organization’s management accepts that the system\r\nmeets the organization’s security requirements. ");
                     
                        System.out.println("" +  PMS.getMP());    
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                        System.out.println();
                        System.out.println( "TO CONTINUE WITH NEXT PLANNING-&-MANAGING-EMAIL-SERVERS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 8");
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                     
                     }
                     
                     else
                     
                        if ( menuSelect == 4)
                        
                        {
                           System.out.println();
                           System.out.println("SYSTEM-SECURITY-PLAN: ");
                           System.out.println();
                        
                           PMS.setSSP("The objective of system security planning is to improve protection of information system resources.\r\nPlans that adequately protect information assets require managers and information owners—directly\r\naffected by and interested in the information and/or processing capabilities—to be convinced that their\r\ninformation assets are adequately protected from loss, misuse, unauthorized access or modification,\r\nunavailability, and undetected activities.\r\n\r\nThe purpose of the system security plan is to provide an overview of the security and privacy\r\nrequirements of the system and describe the controls in place or planned for meeting those requirements.\r\nThe system security plan also delineates responsibilities and expected behavior of all individuals who\r\naccess the system. The system security plan should be viewed as documentation of the structured process\r\nof planning adequate, cost-effective security protection for a system. It should reflect input from various\r\nmanagers with responsibilities concerning the system, including information owners, the system owner,\r\nand the senior agency information security officer (SAISO).\r\n\r\nFor Federal agencies, all information systems must be covered by a system security plan. Other\r\norganizations should strongly consider the completion of a system security plan for each of their systems\r\nas well. The information system owner25 is generally the party responsible for ensuring that the security\r\nplan is developed and maintained and that the system is deployed and operated according to the agreedupon security requirements.\r\n\r\nIn general, an effective system security plan should include the following:\r\n\r\n System Identification. The first sections of the system security plan provide basic identifying\r\ninformation about the system. They contain general information such as the key points of contact for\r\nthe system, the purpose of the system, the sensitivity level of the system, and the environment in\r\nwhich the system is deployed.\r\n\r\n- Controls. This section of the plan describes the control measures (in place or planned) that are\r\nintended to meet the protection requirements of the information system. Controls fall into three\r\ngeneral categories:\r\n\r\n– Management controls, which focus on the management of the computer security system and the\r\nmanagement of risk for a system.\r\n\r\n– Operational controls, which are primarily implemented and executed by people (as opposed to\r\nsystems). They often require technical or specialized expertise, and often rely upon management\r\nactivities as well as technical controls.\r\n\r\n– Technical controls, which are security mechanisms that the computer system employs. The\r\ncontrols can provide automated protection from unauthorized access or misuse, facilitate\r\ndetection of security violations, and support security requirements for applications and data. The\r\nimplementation of technical controls, however, always requires significant operational\r\nconsiderations and should be consistent with the management of security within the organization.  ");
                        
                           System.out.println("" + PMS.getSSP());      
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                           System.out.println();
                           System.out.println( "TO CONTINUE WITH NEXT PLANNING-&-MANAGING-EMAIL-SERVERS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 8");
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                        
                        }
                        
                        else
                        
                           if ( menuSelect == 5)
                           
                           {
                              System.out.println();         
                              System.out.println();
                              System.out.println("HUMAN-RESOURCES-REQUIREMENTS:"); 
                              System.out.println();     
                           
                           
                              PMS.setHRR("When considering the human resource implications of developing and deploying a mail server,\r\norganizations should address the following in the deployment plan:\r\n\r\n- Required Personnel – What types of personnel are going to be required? This would include such\r\npositions as system and mail server administrators, network administrators, and ISSOs.\r\n\r\n- Required Skills – What are the required skills to adequately plan, develop, and maintain the mail\r\nserver in a secure manner? Examples include operating system administration, network\r\nadministration, active content expertise, and programming.\r\n\r\n- Available Personnel – What are the available human resources within the organization? In addition,\r\nwhat are their current skill sets and are they sufficient for supporting the mail server? Often an\r\norganization discovers that its existing human resources are not sufficient and needs to consider the\r\nfollowing options:\r\n\r\n– Train Current Staff – If there are personnel available but they do not have the requisite skills, the\r\norganization may choose to train the existing staff in the skills required. While this is an\r\nexcellent option, the organization should ensure that employees meet all prerequisites for training.\r\n\r\n– Hire Additional Staff – If there is not enough staff available or they do not have the requisite\r\nskills, it may be necessary to hire additional personnel.\r\nOnce the organization has staffed the project and the mail server is active, it will be necessary to ensure\r\nthe number and skills of the personnel are still adequate. The threat and vulnerability levels of hosts\r\nincluding mail servers are constantly changing, as is the technology. This means that what is adequate\r\ntoday may not be tomorrow.");
                           
                           
                              System.out.println("" + PMS.getHRR());
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                              System.out.println();
                              System.out.println( "TO CONTINUE WITH NEXT PLANNING-&-MANAGING-EMAIL-SERVERS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 8");
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                           
                           }
                           
                           else
                           
                              if ( menuSelect == 6)
                              
                              {
                                 System.out.println();         
                                 System.out.println();
                                 System.out.println   ("GENERAL-INFORMATION-SYSTEM-SECURITY-PRINCIPLES:");          
                                 PMS.setGISSP         ("When addressing mail server security issues, it is an excellent idea to keep some general information\r\nsecurity principles in mind:\r\n\r\n- Simplicity—Security mechanisms (and the information systems in general) should be as simple as\r\npossible. Complexity is at the root of many security issues.\r\n\r\n- Fail-Safe—If a failure occurs, the system should fail in a secure manner by which security controls\r\nand settings remain in effect and are enforced. It is usually better to lose functionality rather than\r\nsecurity.\r\n\r\n- Complete Mediation—Rather than providing direct access to information, mediators that enforce\r\naccess policy should be employed. Common examples include file system permissions, proxies,\r\nfirewalls, and mail gateways.\r\n\r\nOpen Design—System security should not depend on the secrecy of the implementation or its\r\ncomponents. “Security through obscurity” is not reliable.\r\n\r\n- Separation of Privilege—Functions, to the degree possible, should be separate and provide as much\r\ngranularity as possible. The concept can apply to both systems and operators/users. In the case of\r\nsystems, such functions such as read, edit, write, and execute should be separate. In the case of\r\nsystem operators and users, roles should be as separate as possible. For example, if resources allow,\r\nthe role of system administrator should be separate from that of the security administrator.\r\n\r\n- Least Privilege—This principle dictates that each task, process, or user is granted the minimum\r\nrights required to perform its job. By applying this principle consistently, should a task, process, or\r\nuser be compromised, the scope of damage is constrained to the limited resources available to the\r\ncompromised entity.\r\n\r\n- Psychological Acceptability—Users should understand the necessity of security. This can be\r\nprovided through training and education. In addition, the security mechanisms in place should\r\npresent users with sensible options that give them the usability they require on a daily basis. If users\r\nfind the security mechanisms too cumbersome, they may devise ways to work around or compromise\r\nthem. The objective is not to weaken security so it is understandable and acceptable, but to train,\r\neducate, and design security mechanisms and policies that are usable and effective.\r\n\r\n- Least Common Mechanism—When providing a feature to the system, it is best to have a process or\r\nservice gain some function without granting the same function to other parts of the system. The\r\nability for the mail server process to access a backend database, for instance, should not also enable\r\nother applications on the system to access the backend database.\r\n\r\n-  Defense in Depth—Organizations should understand that a single security mechanism would\r\ngenerally prove insufficient. Security mechanisms (defenses) need to be layered so that compromise\r\nof a single security mechanism is insufficient to compromise a host or network. There is no “silver\r\nbullet” for information system security.\r\n\r\n- Work Factor—Organizations should understand what it would take to break the system or network’s\r\nsecurity features. The amount of work necessary for an attacker to break the system or network\r\nshould exceed the value that the attacker would gain from a successful compromise.\r\n\r\n- Compromise Recording—Records and logs should be maintained so that if a compromise does\r\noccur, evidence of the attack is available to the organization. This information can assist in securing\r\nthe network and host after the compromise and assist in identifying the methods and exploits used by\r\nthe attacker. This information can be used to better secure the host or network in the future. In\r\naddition, this can assist organizations in identifying and prosecuting attackers.\r\n\r\n");
                                 System.out.println("" + PMS.getGISSP());
                                 System.out.println();
                                 System.out.println("************************************************************************************************" );
                                 System.out.println();
                                 System.out.println( "TO CONTINUE WITH NEXT PLANNING-&-MANAGING-EMAIL-SERVERS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 8");
                                 System.out.println();
                                 System.out.println("************************************************************************************************" );
                              
                              }
                              
                              else
                              
                                 if ( menuSelect == 7)
                                 
                                 {
                                    System.out.println();         
                                    System.out.println();
                                    System.out.println("CHECKLIST-FOR-PLANNING-AND-MANAGING-SERVERS: "); 
                                    System.out.println();     
                                 
                                 
                                    PMS.setCPMS("- Plan the installation and deployment of mail server\r\n- Identify functions of the mail server\r\n- Identify categories of information that will be stored on, processed on, and\r\ntransmitted through the mail server\r\n- Identify security requirements of information\r\n- Identify requirements for continuity of mail services\r\n- Identify a dedicated host to run the mail server\r\n- Identify network services that will be provided or supported by the mail server\r\n- Identify users and categories of users of the mail server and determine privilege\r\nfor each category of user\r\n- Determine how the mail server will be managed (e.g., locally, remotely)\r\n- Identify user authentication methods for the mail server\r\n- Identify security or privacy requirements for email address-related information\r\n- Choose appropriate operating system for mail server\r\n- Minimal exposure to vulnerabilities\r\n- Ability to restrict administrative or root level activities to authorized users only\r\n- Ability to deny access to information on the server other than that intended to\r\nbe available\r\n- Ability to disable unnecessary network services that may be built into the\r\noperating system or server software\r\n- Ability to log appropriate server activities to detect intrusions and attempted\r\nintrusions\r\n- Availability of trained, experienced staff to administer the server and server\r\nproducts\r\n- Plan the location of the mail server\r\n- Appropriate physical security protection mechanisms\r\n- Appropriate environmental controls to maintain the necessary temperature and\r\nhumidity\r\n- Backup power source\r\n- Preparation for known natural disasters. ");
                                 
                                 
                                    System.out.println(" " + PMS.getCPMS());
                                    System.out.println();
                                    System.out.println("************************************************************************************************" );
                                    System.out.println();
                                    System.out.println( "TO CONTINUE WITH NEXT PLANNING-&-MANAGING-EMAIL-SERVERS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 8");
                                    System.out.println();
                                    System.out.println("************************************************************************************************" );
                                 
                                 }
                                 
                                 else
                                 
                                    System.out.println();
               System.out.println   ("HERE ARE EMAIL-ISOLATION-FRAMEWORK MAIN MENU CATEGORIES LIST: ");
               System.out.println();
               System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
               System.out.println();
               System.out.println   ("2.  EMAIL STANDARDS ."); 
               System.out.println();
               System.out.println   ("3.  EMAIL SECURITY THREATS."); 
               System.out.println();
               System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
               System.out.println();
               System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
               System.out.println();
               System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
               System.out.println();
               System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
               System.out.println();
               System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
               System.out.println();
               System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
               System.out.println();
               System.out.println   ("12. SECURING EMAIL CLIENTS."); 
               System.out.println();
               System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
               System.out.println();
               System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
               System.out.println();
               System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
            
               menuSelection = keyboard.nextInt();
            
               while (menuSelection < 1 || menuSelection > 17) 
               
               {
               
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();  
                  System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("HERE IS THE VALID LIST OF EMAIL-ISOLATION MAIN MENU CATEGORIES: ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
                  System.out.println();
                  System.out.println   ("2.  EMAIL STANDARDS ."); 
                  System.out.println();
                  System.out.println   ("3.  EMAIL SECURITY THREATS."); 
                  System.out.println();
                  System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
                  System.out.println();
                  System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
                  System.out.println();
                  System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
                  System.out.println();
                  System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
                  System.out.println();
                  System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
                  System.out.println();
                  System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
                  System.out.println();
                  System.out.println   ("12. SECURING EMAIL CLIENTS."); 
                  System.out.println();
                  System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
                  System.out.println();
                  System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
                  System.out.println();
                  System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
               
               
               
                  menuSelection = keyboard.nextInt();
               
               } 
            
               break;
         
            case 9:
            
               EmailIsolationSetter SOS;
               SOS = new EmailIsolationSetter();
            
            
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println("YOU SELECTED SECURING-THE-EMAIL-SERVERS-OPERATING-SYSTEM CATEGORY FROM EMAIL-ISOLATION MAIN MENU ");
               System.out.println();
               System.out.println("PLEASE SEE BELOW SECURING-THE-EMAIL-SERVERS-OPERATING-SYSTEMS SUBCATEGORIES: ");
               System.out.println(); 
               System.out.println("1.  UPDATING AND CONFIGUTRING THE OPERATING SYSTEM.");
               System.out.println();
               System.out.println("2.  SECURITY TESTING THE OPERATING SYSTEM.");
               System.out.println();
               System.out.println("3.  CHECKLIST FOR SECURING THE MAIL SERVER OPERATING SYSTEM.");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER YOUR SECURING-THE-EMAIL-SERVERS-OPERATING-SYSTEM CHOICE (1 to 3): ");
            
            
               menuSelect = keyboard.nextInt();
            
               while (menuSelect < 1 || menuSelect > 3)
               
               {
               
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println("THIS IS INVALID CHOICE FOR SECURING-THE-EMAIL-SERVERS-OPERATING-SYSTEM SELECTION "); 
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW VALID SECURING-THE-EMAIL-SERVERS-OPERATING-SYSTEM SELECTIONS:");
                  System.out.println();
                  System.out.println("1.  UPDATING AND CONFIGUTRING THE OPERATING SYSTEM.");
                  System.out.println();
                  System.out.println("2.  SECURITY TESTING THE OPERATING SYSTEM.");
                  System.out.println();
                  System.out.println("3.  CHECKLIST FOR SECURING THE MAIL SERVER OPERATING SYSTEM.");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER YOUR SECURING-THE-EMAIL-SERVERS-OPERATING-SYSTEM CATEGORIES CHOICE (1 to 3): ");
               
               
                  menuSelect = keyboard.nextInt();
               
               }
            
            //System.out.println();
            //System.out.println(" NOTE: There are eight performance attributes, or currencies, to be considered when evaluating whether a EMAIL-ISOLATION network can deliver on its full potential.".toUpperCase());
            //System.out.println();                
            //System.out.println(" NOTE:  Without all eight of these currencies, you don’t have a true EMAIL-ISOLATION network. With them, you have a powerful, game-changing platform for innovation .".toUpperCase());
            // System.out.println(); 
            
               if ( menuSelect == 1)
               
               {          
                  System.out.println();
                  System.out.println("UPDATING-AND-CONFIGUTRING-THE-OPERATING-SYSTEM: ");
                  System.out.println();
               
               
                  SOS.setUCOS           ("Patch and Upgrade Operating System\r\n\r\nOnce an operating system is installed, applying needed patches or upgrades to correct for known\r\nvulnerabilities is essential. Any operating system has known vulnerabilities that should be corrected\r\nbefore using it to host a mail server. To adequately detect and correct these vulnerabilities, mail server\r\nadministrators should do the following:\r\n\r\n- Create and implement a patching process\r\n\r\n- Identify vulnerabilities and applicable patches\r\n\r\n- Mitigate vulnerabilities temporarily if needed and if feasible (until patches are available, tested, and installed)\r\n\r\n- Install permanent fixes (often called patches, hotfixes, service packs, or updates).\r\n\r\nAdministrators should ensure that mail servers, particularly new ones, are adequately protected during the\r\npatching process. For example, a mail server that is not fully patched or not configured securely could be\r\ncompromised by threats if it is publicly accessible while it is being patched. When preparing new mail\r\nservers for deployment, administrators should do either of the following:\r\n\r\n- Keep the servers disconnected from networks or connect them only to an isolated “build” network\r\nuntil all patches have been transferred to the servers through out-of-band means (e.g., CDs) and\r\ninstalled, and the other configuration steps listed in Section 5.1 have been performed.\r\n\r\n- Place the servers on a virtual local area network (VLAN) or other network segment that severely\r\nrestricts what actions the hosts on it can perform and what communications can reach the hosts—only\r\nallowing those events that are necessary for patching and configuring the hosts. Do not transfer the\r\nhosts to regular network segments until all the configuration steps have been\r\n performed.\r\n\r\nAdministrators should generally not apply patches to mail servers without first testing them on another\r\nidentically configured server, because patches can inadvertently cause operational problems. Although\r\nadministrators can configure mail servers to download patches automatically, the servers should not be\r\nconfigured to install them automatically so that they can first be tested.\r\n\r\nRemove or Disable Unnecessary Services and Applications\r\n\r\nIdeally, a mail server should be on a dedicated, single-purpose host. When configuring the operating\r\nsystem, disable everything except that which is expressly permitted – that is, disable all services and\r\napplications, enable only those required by the mail server, and then remove the unneeded services and\r\napplications. If possible, install the minimal operating system configuration that is required for the mail\r\nserver application. Choose the “minimal installation” option, if available, to minimize the effort required\r\nin removing unnecessary services. In addition, many uninstall scripts or programs are far from perfect in\r\ncompletely removing all components of a service; therefore, it is always better not to install unnecessary\r\nservices. Some common types of services and applications that should usually be disabled if not required\r\ninclude the following:\r\n\r\n- File and printer sharing services (e.g., Windows Network Basic Input/Output System file\r\nand printer sharing, Network File System [NFS], File Transfer Protocol [FTP])\r\n\r\n- Default Web servers\r\n\r\n- Wireless networking services\r\n\r\n-Remote control and remote access programs, particularly those that do not strongly encrypt their\r\ncommunications (e.g., Telnet)\r\n\r\n-Directory services (e.g., Lightweight Directory Access Protocol [LDAP], Kerberos, Network\r\nInformation System [NIS])\r\n\r\n- Language compilers and libraries\r\n\r\n- System development tools\r\n\r\n- System and network management tools and utilities, including Simple Network Management Protocol(SNMP).\r\n\r\nRemoving unnecessary services and applications is preferable to simply disabling them through\r\nconfiguration settings, because attacks that attempt to alter settings and activate a disabled service cannot\r\nsucceed when the functional components are completely removed. Disabled services could also be\r\nenabled inadvertently through human error.\r\n\r\nEliminating or disabling unnecessary services enhances the security of a mail server in several ways:\r\n\r\n- Other services cannot be compromised and used to attack the host or impair the services of the mail\r\nserver. Each service added to a host increases the risk of compromise for that host because each\r\nservice is another possible avenue of access for an attacker. Less is more secure in this case.\r\n\r\n- Other services might have flaws or might be incompatible with the mail server itself. Disabling or\r\nremoving them prevents them from affecting the mail server, including its availability.\r\n\r\n- The host can be configured to better suit the requirements of the particular service. Different services\r\nmight require different hardware and software configurations, which could lead to unnecessary\r\nvulnerabilities or negatively affect performance.\r\n\r\n- By reducing services, the number of logs and log entries is reduced; therefore, detecting unexpected\r\nbehavior becomes easier.\r\n\r\nOrganizations should determine the services to be enabled on a mail server. Services in addition to the\r\nmail server service that might be installed include directory protocols to access the organization’s user\r\ndirectory and remote administration services. These services may be required in certain instances, but\r\nthey may increase the risks to the server. Whether the risks outweigh the benefits is a decision for each\r\norganization to make.\r\n\r\nIf Web-based mail access is to be provided, the Web server running the mail application should be on a\r\nseparate host from the mail server. Having the Web and mail servers on separate hosts limits the impact\r\nif one of them is compromised when compared with having both servers on the same host. The benefits\r\nof the latter arrangement are efficient and protected communications, because the Web and mail servers\r\ncommunicate directly within a host instead of over a network.\r\nConfigure Operating System User Authentication\r\n\r\nFor mail servers, the authorized users who can configure the operating system are limited to a small\r\nnumber of designated mail server administrators. The users who can access the mail server, however,\r\nmay range from unrestricted to restricted subsets of the organization’s employees. To enforce policy\r\nrestrictions, if required, the mail server administrator must configure the operating system to authenticate\r\na prospective user by requiring proof that the user is authorized for such access.\r\n\r\nEnabling authentication by the host computer involves configuring parts of the operating system,\r\nfirmware, and applications, such as the software that implements a network service. In special cases, for\r\nhigh-value/high-risk sites, organizations may also use authentication hardware, such as tokens or one-time\r\npassword devices. Use of authentication mechanisms where authentication information is reusable (e.g.,\r\npasswords) and transmitted in the clear over a network is strongly discouraged, because the informationan be intercepted and used by an attacker to masquerade as an authorized user.\r\n\r\nTo ensure the appropriate user authentication is in place, take the following steps:\r\n\r\n- Remove or disable unneeded default accounts and groups. The default configuration of the\r\n\r\noperating system often includes guest accounts (with and without passwords), administrator or root\r\nlevel accounts, and accounts associated with local and network services. The names and passwords\r\nfor those accounts are well known. Remove or disable unnecessary accounts to eliminate their use by\r\nattackers, including guest accounts on computers containing sensitive information. If there is a\r\nrequirement to retain a guest account or group, severely restrict its access and change the default\r\npassword in accordance with the organizational password policy. For default accounts that need to be\r\nretained, change the names (where possible and particularly for administrator or root level accounts)\r\nand passwords to be consistent with the organizational password policy. Default account names andasswords are commonly known in the attacker community.\r\n\r\n- Disable non-interactive accounts. Disable accounts (and the associated passwords) that need to\r\nexist but do not require an interactive login. For Unix systems, disable the login shell or provide a\r\nlogin shell with NULL functionality (e.g., /bin/false).\r\n\r\n- Create the user groups. Assign users to the appropriate groups. Then assign rights to the groups, as\r\ndocumented in the deployment plan. This approach is preferable to assigning rights to individual\r\nusers because the latter becomes unwieldy with large numbers of users.\r\n\r\n- Create the user accounts. The deployment plan identifies who will be authorized to use each\r\ncomputer and its services. Create only the necessary accounts. Permit the use of shared accounts\r\nonly when no viable alternatives exist.\r\n\r\n- Check the organization’s password policy. Set account passwords appropriately. This policy\r\nshould address the following areas:\r\n\r\n– Length – a minimum length for passwords. Specify a minimum length of at least eight characters.\r\n\r\n– Complexity – the mix of characters required. Require passwords to contain both uppercase and\r\nlowercase letters and at least one non-alphanumeric character, and to not be a “dictionary”\r\n\r\n– Aging – how long a password may remain unchanged. Require users to change their passwords\r\nperiodically. Administrator or root level passwords should be changed every 30 to 120 days.\r\nUser level passwords should also be changed periodically, with the period determined by the\r\nenforced length and complexity of the password combined with the sensitivity of the information\r\nprotected. When considering the appropriate aging duration, the exposure level of user\r\npasswords should also be taken into account.\r\n\r\n– Reuse – whether a password may be reused. Some users try to defeat a password aging\r\nrequirement by changing the password to one they have used previously. If possible, ensure that\r\nusers cannot change their password by merely appending characters to the beginning or end of\r\ntheir original password (e.g., original password was “mysecret” and is changed to “1mysecret” or\r\n“mysecret1”).\r\n\r\n– Authority – who is allowed to change or reset passwords and what sort of proof is required\r\nbefore initiating any changes.\r\n\r\n– Password Security – how passwords should be secured, such as not storing passwords\r\nunencrypted on the mail server, and requiring administrators to use different passwords for their\r\nmail administration accounts than their other administration accounts.\r\n\r\n- Configure computers to prevent password guessing. It is relatively easy for an unauthorized user\r\nto try to gain access to a computer by using automated software tools that attempt all passwords. If\r\nthe operating system provides the capability, configure it to increase the period between login\r\nattempts with each unsuccessful attempt. If that is not possible, the second alternative is to deny login\r\nafter a limited number of failed attempts (e.g., three). Typically, the account is “locked out” for a\r\nperiod of time (such as 30 minutes) or until a user with appropriate authority reactivates it.\r\n\r\nThe choice to deny login is another situation that requires the mail server administrator to make a\r\ndecision that balances security and convenience. Implementing this recommendation can help\r\nprevent some kinds of attacks, but it can also allow an attacker to make failed login attempts to\r\nprevent user access, a denial of service (DoS) condition.\r\n\r\nFailed network login attempts should not prevent an authorized user or administrator from logging in\r\nat the console. Note that all failed login attempts whether via the network or console should be\r\nlogged. If remote administration is not to be implemented, disable the ability for the\r\nadministrator or root level accounts to log in from the network.\r\n\r\n- Install and configure other security mechanisms to strengthen authentication. If the information\r\non the mail server requires it, consider using other authentication mechanisms such as biometrics,\r\nsmart cards, client/server certificates, or one-time password systems. They can be more expensive\r\nand difficult to implement, but they may be justified in some circumstances. When such\r\nauthentication mechanisms and devices are used, the organization’s policy should be changed\r\naccordingly.\r\n\r\nAs mentioned earlier, attackers using network sniffers can easily capture passwords passed across a\r\nnetwork in clear text. However, passwords are economical and appropriate if properly protected while in\r\ntransit. Implement authentication and encryption technologies, such as Secure Sockets Layer\r\n(SSL)/Transport Layer Security (TLS), Secure Shell (SSH), or Virtual Private Networks (VPNs) (for\r\nremote users), to protect passwords during transmission. Requiring server side authentication to be used\r\nwith encryption technologies reduces the likelihood of successful man-in-the-middle attacks.\r\n\r\n Configure Resource Controls Appropriately\r\n\r\nAll commonly used modern server operating systems provide the capability to specify access privileges\r\nindividually for files, directories, devices, and other computational resources. By carefully setting access\r\ncontrols and denying personnel unauthorized access, the mail server administrator can reduce security\r\nbreaches. For example, denying read access to files and directories helps to protect confidentiality of\r\ninformation, and denying unnecessary write (modify) access can help maintain the integrity of\r\ninformation. Limiting the execution privilege of most system-related tools to authorized system\r\nadministrators can prevent users from making configuration changes that could reduce security. It also\r\ncan restrict the attacker’s ability to use those tools to attack the system or other systems on the network.\r\n\r\nInstall and Configure Additional Security Controls\r\n\r\nOperating systems often do not include all of the security controls necessary to secure the operating\r\nsystem, services, and applications adequately. In such cases, administrators need to select, install, and\r\nconfigure additional software to provide the missing controls. Commonly needed controls include the\r\nfollowing:\r\n\r\n- Anti-malware software, such as anti-virus software, anti-spyware software, and rootkit detectors, to\r\nprotect the local operating system from malware and to detect and eradicate any infections that\r\noccur. Examples of when anti-malware software would be helpful include a mail administrator\r\nbringing infected media to the mail server and a network service worm contacting the server and\r\ninfecting it. This software is independent of the anti-malware software used to scan the email passing\r\nthrough the server. For many mail systems, anti-virus software is the only form of anti-malware\r\nsoftware needed to protect the OS.\r\n\r\n- Host-based intrusion detection and prevention software, to detect attacks performed against the mail\r\nservers. Section 7.2.2 contains additional information on host-based intrusion detection and\r\nprevention software.\r\n\r\n- Host-based firewalls, to protect the server from unauthorized access.\r\n\r\n- Patch management software, to ensure that vulnerabilities are addressed promptly. Patch\r\n\r\nmanagement software can be used just to apply patches, or also to identify new vulnerabilities in the\r\nmail server’s operating systems, services, and applications.\r\nSome mail server administrators also install one or more forms of host-based intrusion detection software\r\non their servers. For example, file integrity checking software can identify changes to critical system files.\r\n\r\nWhen planning security controls, mail server administrators should consider the resources that the\r\nsecurity controls will consume. A server’s performance could degrade if it does not have enough memory\r\nand processing capacity for the controls.");
               
               
                  System.out.println        ("" +  SOS.getUCOS());
                  System.out.println();          
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println( "TO CONTINUE WITH NEXT UPDATING-AND-CONFIGUTRING-THE-OPERATING-SYSTEM CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU  CHOICE # 9");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
               
               }
               
               else
               
                  if ( menuSelect == 2)
                  
                  {
                     System.out.println();
                     System.out.println();
                     System.out.println("SECURITY-TESTING-THE-OPERATING-SYSTEM: ");
                     System.out.println();
                  
                     SOS.setSTOS ("Security Testing the Operating System:\r\n\r\nPeriodic security testing of the operating system is a vital way to identify vulnerabilities and to ensure that\r\nthe existing security precautions are effective. Methods for testing operating systems include\r\nvulnerability scanning and penetration testing. Vulnerability scanning usually entails using an automated\r\nvulnerability scanner to scan a host or groups of hosts on a network for application, network, and\r\noperating system vulnerabilities. Penetration testing is a testing process designed to compromise a\r\nnetwork using the tools and methodologies of an attacker. It involves iteratively identifying and\r\nexploiting the weakest areas of the network to gain access to the remainder of the network, eventually\r\ncompromising the overall security of the network. Vulnerability scanning should be conducted\r\nperiodically, such as weekly or monthly, and penetration testing should be conducted at least annually.\r\nBecause both of these testing techniques also are applicable to testing the mail server application.");
                  
                  
                  
                     System.out.println("" +  SOS.getSTOS());
                     System.out.println();
                     System.out.println("************************************************************************************************" );
                     System.out.println();
                     System.out.println( "TO CONTINUE WITH NEXT UPDATING-AND-CONFIGUTRING-THE-OPERATING-SYSTEM CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 9");
                     System.out.println();
                     System.out.println("************************************************************************************************" );   
                  
                  }
                  
                  else
                  
                     if ( menuSelect == 3 )
                     
                     {
                        System.out.println();
                        System.out.println();
                        System.out.println("CHECKLIST-FOR-SECURING-THE-MAIL-SERVER-OPERATING-SYSTEM: ");
                        System.out.println();  
                     
                        SOS.setCSMO("- Patch and upgrade operating system\r\n\r\n- Create and implement a patching process\r\n\r\n- Identify, test, and install all necessary patches and upgrades to the operating system\r\n\r\n- Remove or disable unnecessary services and applications\r\n\r\n- Remove or disable unnecessary services and applications\r\n\r\n- Use separate hosts for Web servers, directory servers, and other services\r\n\r\n- Configure operating system user authentication\r\n\r\n- Remove or disable unneeded default accounts and groups\r\n\r\n- Disable non-interactive accounts\r\n\r\n- Create the user groups for the particular computer\r\n\r\n- Create the user accounts for the particular computer\r\n\r\n- Check the organization’s password policy, and set account passwords\r\n\r\n- appropriately (e.g., length, complexity)\r\n\r\n- Configure computers to prevent password guessing\r\n\r\n- Install and configure other security mechanisms to strengthen authentication\r\n\r\n- Configure resource controls appropriately\r\n\r\n- Set access controls for files, directories, devices, and other resources\r\n\r\n- Limit privileges for most system-related tools to authorized system administrators\r\n\r\n- Install and configure additional security controls\r\n\r\n- Select, install, and configure additional software to provide needed controls not\r\n\r\n- included in the operating system\r\n\r\n- Test the security of the operating system\r\n\r\n- Test operating system after initial install to determine vulnerabilities\r\n\r\n- Test operating system periodically to determine new vulnerabilities");
                     
                        System.out.println("" +  SOS.getCSMO());    
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                        System.out.println();
                        System.out.println( "TO CONTINUE WITH NEXT UPDATING-AND-CONFIGUTRING-THE-OPERATING-SYSTEM CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 9");
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                     
                     }
                     
                     
                     
                     else
                     
               System.out.println();
               System.out.println   ("HERE ARE EMAIL-ISOLATION-FRAMEWORK MAIN MENU CATEGORIES LIST: ");
               System.out.println();
               System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
               System.out.println();
               System.out.println   ("2.  EMAIL STANDARDS ."); 
               System.out.println();
               System.out.println   ("3.  EMAIL SECURITY THREATS."); 
               System.out.println();
               System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
               System.out.println();
               System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
               System.out.println();
               System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
               System.out.println();
               System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
               System.out.println();
               System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
               System.out.println();
               System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
               System.out.println();
               System.out.println   ("12. SECURING EMAIL CLIENTS."); 
               System.out.println();
               System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
               System.out.println();
               System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
               System.out.println();
               System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
            
               menuSelection = keyboard.nextInt();
            
               while (menuSelection < 1 || menuSelection > 17) 
               
               {
               
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();  
                  System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("HERE IS THE VALID LIST OF EMAIL-ISOLATION MAIN MENU CATEGORIES: ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
                  System.out.println();
                  System.out.println   ("2.  EMAIL STANDARDS ."); 
                  System.out.println();
                  System.out.println   ("3.  EMAIL SECURITY THREATS."); 
                  System.out.println();
                  System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
                  System.out.println();
                  System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
                  System.out.println();
                  System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
                  System.out.println();
                  System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
                  System.out.println();
                  System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
                  System.out.println();
                  System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
                  System.out.println();
                  System.out.println   ("12. SECURING EMAIL CLIENTS."); 
                  System.out.println();
                  System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
                  System.out.println();
                  System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
                  System.out.println();
                  System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
               
               
               
                  menuSelection = keyboard.nextInt();
               
               } 
            
               break;
         
            case 10:
            
               EmailIsolationSetter SESC;
               SESC = new EmailIsolationSetter();
            
            
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println("YOU SELECTED SECURING-EMAIL-SERVERS-AND-CONTENT CATEGORY FROM EMAIL-ISOLATION MAIN MENU ");
               System.out.println();
               System.out.println("PLEASE SEE BELOW SECURING-EMAIL-SERVERS-AND-CONTENT CATEGORIES: ");
               System.out.println(); 
               System.out.println("1.  HARDENING THE MAIL SERVER APPLICATION .");
               System.out.println();
               System.out.println("2.  PROTECTING EMAIL FROM MALWARE.");
               System.out.println();
               System.out.println("3.  BLOCKING SPAM-SENDING SERVERS.");
               System.out.println();
               System.out.println("4.  AUTHENTICATED MAIL RELAY.");
               System.out.println();
               System.out.println("5.  SECURE ACCESS.");
               System.out.println();
               System.out.println("6.  ENABLING WEB ACCESS.");
               System.out.println();
               System.out.println("7.  CHECKLIST FOR SECURING MAIL SERVERS AND CONTENT.");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER YOUR SECURING-EMAIL-SERVERS-AND-CONTENT CHOICE (1 to 7): ");
            
            
               menuSelect = keyboard.nextInt();
            
               while (menuSelect < 1 || menuSelect > 7)
               
               {
               
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println("THIS IS INVALID CHOICE FOR SECURING-EMAIL-SERVERS-AND-CONTENT SELECTION "); 
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW VALID SECURING-EMAIL-SERVERS-AND-CONTENT SELECTIONS:");
                  System.out.println();
                  System.out.println("1.  HARDENING THE MAIL SERVER APPLICATION .");
                  System.out.println();
                  System.out.println("2.  PROTECTING EMAIL FROM MALWARE.");
                  System.out.println();
                  System.out.println("3.  BLOCKING SPAM-SENDING SERVERS.");
                  System.out.println();
                  System.out.println("4.  AUTHENTICATED MAIL RELAY.");
                  System.out.println();
                  System.out.println("5.  SECURE ACCESS.");
                  System.out.println();
                  System.out.println("6.  ENABLING WEB ACCESS.");
                  System.out.println();
                  System.out.println("7.  CHECKLIST FOR SECURING MAIL SERVERS AND CONTENT.");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER YOUR SECURING-EMAIL-SERVERS-AND-CONTENT CHOICE (1 to 7): ");
               
               
               
                  menuSelect = keyboard.nextInt();
               
               }
            
             /*System.out.println();
               System.out.println(" NOTE: There are eight performance attributes, or currencies, to be considered when evaluating whether a EMAIL-ISOLATION network can deliver on its full potential.".toUpperCase());
               System.out.println();                
               System.out.println(" NOTE:  Without all eight of these currencies, you don’t have a true EMAIL-ISOLATION network. With them, you have a powerful, game-changing platform for innovation .".toUpperCase());
               System.out.println(); 
               */
               
               if ( menuSelect == 1)
               
               {          
                  System.out.println();
                  System.out.println("HARDENING-THE-MAIL-SERVER-APPLICATION: ");
                  System.out.println();
               
               
                  SESC.setHMSA           ("Hardening mail server applications is an important step in protecting mail servers from compromise. This\r\nsection provides recommendations for securely installing mail servers and configuring operating system\r\nand mail server access controls. Another important part of mail security is protecting the email content\r\nthat traverses the server, which includes content filtering, malware scanning, and spam prevention.\r\nSecuring access to mailboxes by encrypting communications, including Web-based mail access, is also\r\naddressed in this section. Email content security can also involve email encryption to preserve\r\nconfidentiality and digital signatures to support integrity and non-repudiation; these are discussed in\r\n\r\nHardening the Mail Server Application\r\n\r\nAfter ensuring that the mail server’s operating system is secured properly, the next step is to install the\r\nmail server application and secure it from likely threats. The subsections that follow provide an overview of these two actions.\r\n\r\nSecurely Installing the Mail Server\r\n\r\nIn many respects, the secure installation and configuration of the mail server application mirrors the\r\noperating system process.The overarching principle, as before, is to install only\r\nthe services required for the mail server and to eliminate any known vulnerabilities through patches or\r\nupgrades. Any unnecessary applications, services, or scripts that are installed should be removed\r\nimmediately once the installation process is complete. During the installation of the mail server, the\r\nfollowing steps should be performed:\r\n\r\n- Install the mail server software on a dedicated host\r\n\r\n- Apply any patches or upgrades to correct for known vulnerabilities\r\n\r\n- Create a dedicated physical disk or logical partition (separate from operating system and mail server\r\napplication) for mailboxes, or host the mailboxes on a separate server\r\n\r\n- Remove or disable all services installed by the mail server application but not required (e.g., Webbased mail, FTP, remote administration)\r\n\r\n- Remove or disable all unneeded default login accounts created by the mail server installationemove all manufacturer documentation from the server\r\n\r\n- Remove any example or test files from the server\r\n\r\n- Apply appropriate security template or hardening script to the server\r\n\r\n- Reconfigure SMTP, POP, and IMAP service banners (and others as required) NOT to report mail\r\nserver and operating system type and version (this may not be possible with all mail servers)\r\n\r\n- Disable dangerous or unnecessary mail commands (e.g., VRFY and EXPN).\r\n\r\nConfiguring Operating System and Mail Server Access Controls\r\n\r\nMost mail server host operating systems provide the capability to specify access privileges individually\r\nfor files, devices, and other computational resources on that host. Any information that the mail server\r\ncan access using these controls can potentially be distributed to all users accessing the mail server. The\r\nmail server software is likely to include mechanisms to provide additional file, device, and resource\r\naccess controls specific to its operation. It is important to set identical permissions for both the operating\r\nsystem and mail server application; otherwise, too much or too little access may be granted to users. Mail\r\nserver administrators should consider how best to configure access controls to protect information stored\r\non their public mail server from two perspectives:\r\n\r\n- Limit the access of the mail server application to a subset of computational resources\r\n\r\n- Limit the access of users through additional access controls enforced by the mail server, where more\r\ndetailed levels of access control are required.\r\n\r\nThe proper setting of access controls can help prevent the disclosure of sensitive or restricted information\r\nthat is not intended for public dissemination. In addition, access controls can be used to limit resource use\r\nin the event of a DoS attack against the mail server.\r\n\r\nTypical files to which access should be controlled are as follows:\r\n\r\n- Application software and configuration files\r\n\r\n- Files directly related to security mechanisms:\r\n\r\n– Password hash files and other files used in authentication\r\n\r\n– Files containing authorization information used in controlling access\r\n\r\n– Cryptographic key material used in confidentiality, integrity, and non-repudiation services\r\n\r\n--Server log and system audit files\r\n\r\n-- System software and configuration files.\r\n\r\nEnsure that the mail server application executes only under a unique individual user and group identity\r\nwith very restrictive access controls. Thus, new user and group identities to be used exclusively by the\r\nmail server software need to be established. The new user and new group should be independent and\r\nunique from all other users and groups. This is a prerequisite for implementing the access controls\r\ndescribed in the following steps. Although the server may initially have to run with root (Unix) or\r\nadministrator/system (Windows) privileges to bind to the necessary TCP ports, do not allow the server to\r\ncontinue to run at this level of access.\r\n\r\nIn addition, use the mail server operating system to limit files accessed by the mail service processes.\r\nThese processes should have read-only access to those files necessary to perform the service and should\r\nhave no access to other files, such as server log files. Use mail server host operating system access\r\ncontrols to enforce the following:\r\n\r\n- Temporary files created by the mail server application are restricted to a specified and appropriately\r\nprotected subdirectory (if possible).\r\n\r\n- Access to any temporary files created by the mail server application is limited to the mail server\r\nprocesses that created these files (if possible).\r\n\r\nIt is also necessary to ensure that the mail server cannot save files outside the specified file structure\r\ndedicated to the mail server. This may be a configuration choice in the server software, or it may be a\r\nchoice in how the server process is controlled by the operating system. Ensure that such directories and\r\nfiles (outside the specified directory tree) cannot be accessed, even if users know the locations of those files.\r\nOn Linux and Unix hosts, consider using a “chroot jail” for the mail server application. Using chroot\r\nchanges the mail server’s “view” of the host file system such that the apparent root directory is not the\r\nreal file system root directory but rather one of its subparts. Thus, if the mail server is successfully\r\ncompromised, the attacker only gains access to the limited subpart of the file system accessible via chroot.This is a very powerful security measure.\r\n\r\nTo mitigate the effects of certain types of DoS attacks, configure the mail server to limit the amount of\r\noperating system resources it can consume. Some examples include:\r\n\r\n- Installing users’ mailboxes on a different server (preferred), hard drive, or logical partition than the\r\noperating system and mail server application\r\n\r\n- Configuring the mail server application so that it cannot consume all available space on its hard\r\ndrives or partitions\r\n\r\n- Limiting the size of attachments that are allowed\r\n\r\n- Ensuring log files are stored in a location that is sized appropriately.\r\n\r\nTo some degree, these actions protect against attacks that attempt to fill the file system on the mail server\r\nhost operating system with extraneous and incorrect information that may cause the system to crash. This\r\nalso protects against attacks that attempt to fill primary random access memory with unnecessary\r\nprocesses to slow down or crash the system, thus limiting mail server availability. Logging information\r\ngenerated by the mail server host operating system may help in recognizing such attacks. As discussed in\r\nadministrators should store mail server logs on centralized logging servers whenever\r\npossible, and also store logs locally if feasible. If an attack causes the mail server to be compromised, the\r\nattacker could modify or erase locally stored logs to conceal information on the attack. Having a copy of\r\nthe logs on a centralized logging server gives administrators more information to use when investigating\r\nsuch a compromise.");
               
               
                  System.out.println     ("" +  SESC.getHMSA());
                  System.out.println();          
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println( "TO CONTINUE WITH NEXT SECURING-EMAIL-SERVERS-AND-CONTENT CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU  CHOICE # 10");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
               
               }
               
               else
               
                  if ( menuSelect == 2)
                  
                  {
                     System.out.println();
                     System.out.println();
                     System.out.println("PROTECTING-EMAIL-FROM-MALWARE: ");
                     System.out.println();
                  
                     SESC.setPEFM ("Email has increasingly been used as a means for sending binary files in the form of attachments. Initially,\r\nthis did not pose much of a security risk because attachments were mostly small word processing\r\ndocuments or photos. As more organizations began using email for day-to-day collaboration, the size and\r\ntypes of email attachments increased. Today, many email messages are sent with attachments such as\r\nprogram executables, pictures, music, and sounds. Many forms of malware, including viruses, worms,\r\nTrojan horses, and spyware—malware intended to violate a user’s privacy—are often transmitted in\r\nattachments. Increasingly, attackers are using email to deliver zero-day attacks at targeted organizations\r\nbefore these vulnerabilities are known publicly. These attacks are often targeted at office productivity\r\nsoftware and give the attacker control over users’ workstations. This control can be exploited to escalate\r\nprivileges, gain access to sensitive information, monitor users’ actions (e.g., keystrokes), and perform\r\nother malicious actions.\r\n\r\nDetermining whether to allow certain types of attachments can be a difficult decision for an organization.\r\nNot allowing any attachments would simplify a system and make it more secure; however, it would\r\ndramatically reduce its usefulness, and users might employ encoding tricks to work around the restriction\r\nto “get the job done”. Ultimately, organizations choose to allow at least some email attachments.\r\nOrganizations should determine which types of attachments to allow. The simplest approach is to allow\r\nall types of attachments. If this is the case, then some sort of malware scanner (e.g., anti-virus software,\r\nanti-spyware software) should be installed in the mail transit path to filter out known malware, and\r\nperhaps even some behavior blocking utility installed at the client to prevent any unwanted operations by\r\nexecutable attachments from occurring.\r\n\r\nMalware Scanning\r\n\r\nTo protect against viruses, worms, and other forms of malware, it is necessary to implement scanning at\r\none or more points within the email delivery process. Malware scanning can be implemented on the\r\nfirewall, mail relay, or mail gateway appliance as the email data enters the organization’s network, on the\r\nmail server itself, and/or on the end users’ hosts. Each option has its own strengths and weaknesses,\r\nwhich are discussed below. Generally, organizations should implement at least two levels of malware\r\nscanning—one at the end users’ host level and one at the mail server or the firewall/mail relay/mail\r\ngateway level—and should consider implementing malware scanning at all three levels.\r\n\r\nWhen providing multiple layers of malware protection, organizations should consider choosing products\r\nfrom different manufacturers. Diversity increases the chances of blocking the latest threats, because the\r\nresponse time of individual manufacturers to new threats varies. This means that when the newest threats\r\nappear, one product can often detect them earlier than another over some period of time (typically hours,\r\nperhaps a few days). Since each manufacturer uses different detection methods, some products are also\r\nbetter able to detect certain types of new threats than other products.\r\n\r\nScanning at the Firewall, Mail Relay, or Mail Gateway Appliance\r\nThe first option is scanning for malware at the firewall (application proxy), mail relay, or\r\nmail gateway appliance, which can intercept messages before they reach the organization’s mail server.\r\nThe device listens on TCP port 25 for SMTP connections, scans each message, then forwards the\r\nmessages not containing malware to the mail server, which is configured to listen on an unprivileged,\r\nunused port, rather than the usual port 25. A disadvantage to this approach is that constant scanning of\r\nthe SMTP stream can reduce firewall/ mail relay/mail gateway performance. Whether this performance\r\nhit is significant depends on mail load, including both the typical number of emails per day and the peak\r\nrates of emails, and quality of service requirements. One remedy to improve performance is to offload\r\nmalware scanning to a dedicated server.\r\n\r\nThe benefits of scanning email at the firewall, mail relay, or mail gateway appliance are as follows:\r\n\r\n- Can scan email in both directions (inbound and outbound from the organization’s network)\r\n\r\n- Can stop the majority of messages containing malware at the perimeter before they enter the network\r\nand are passed to the mail server\r\n\r\n- Can implement scanning for inbound email with minor changes to the existing mail server\r\nconfiguration\r\n\r\n- Can reduce the amount of email reaching the mail servers, allowing them to operate more efficiently\r\nwith lower operational costs\r\n\r\n- Can reduce the amount of scanning to be performed by the mail servers, thus reducing their load\r\n\r\n- Can centrally manage scanning to ensure compliance with the organization’s security policy and\r\nregular application of updated malicious code signatures\r\n\r\n- For some mail firewall appliances, can provide secure authenticated access to Web-based mail\r\napplications.\r\n\r\nScanning for malware at the firewall, mail relay, or mail gateway appliance has a number of weaknesses:\r\n\r\n- Can require significant modification of the existing mail server configuration when scanning mail in\r\nthe outbound direction\r\n\r\n- Cannot scan encrypted emails \r\n\r\n- Offers no protection to internal users once malware is on the organization’s internal network, unless\r\n\r\n- Offers no protection to internal users once malware is on the organization’s internal network, unless\r\n\r\nthe network is configured so that SMTP traffic gets routed through a dedicated scanner before\r\nreaching the mail serverMay require powerful (expensive) servers or appliances to handle the load of a large organization.\r\n\r\nScanning on the Mail Server Itself\r\n\r\nThe second option for placement of a mail malware scanner is on the mail server itself\r\nMany third-party applications are available to scan the contents of the message stores for most popular\r\nmail servers. These applications inspect the email sent between internal users, which normally do not\r\npass through the organization’s firewall/mail relay/mail gateway. Performing scanning on the mail server\r\nalso provides an additional layer of protection against malware, and also helps to stop internal malware\r\noutbreaks. Some mail servers offer application programming interfaces (API) that support the integration\r\nof malware scanning, content filtering, attachment blocking, and other security services within the MT\r\n\r\n- Offers no protection to internal users once malware is on the organization’s internal network, unlessthe network is configured so that SMTP traffic gets routed through a dedicated scanner before\r\nreaching the mail server\r\n\r\n\r\n- May require powerful (expensive) servers or appliances to handle the load of a large organization.\r\nScanning on the Mail Server Itself\r\nThe second option for placement of a mail malware scanner is on the mail server itself \r\n.Many third-party applications are available to scan the contents of the message stores for most popular\r\nmail servers. These applications inspect the email sent between internal users, which normally do not\r\npass through the organization’s firewall/mail relay/mail gateway. Performing scanning on the mail server\r\nalso provides an additional layer of protection against malware, and also helps to stop internal malware\r\noutbreaks. Some mail servers offer application programming interfaces (API) that support the integration\r\nof malware scanning, content filtering, attachment blocking, and other security services within the MT\r\nthe network is configured so that SMTP traffic gets routed through a dedicated scanner before\r\nreaching the mail server\r\n\r\n- May require powerful (expensive) servers or appliances to handle the load of a large organization.Scanning on the Mail Server Itself\r\nThe second option for placement of a mail malware scanner is on the mail server itself\r\n.Many third-party applications are available to scan the contents of the message stores for most popular\r\nmail servers. These applications inspect the email sent between internal users, which normally do not\r\npass through the organization’s firewall/mail relay/mail gateway. Performing scanning on the mail server\r\nalso provides an additional layer of protection against malware, and also helps to stop internal malware\r\noutbreaks. Some mail servers offer application programming interfaces (API) that support the integration\r\nof malware scanning, content filtering, attachment blocking, and other security services within the MTA\r\n\r\nThe major disadvantage of implementing malware scanning on the mail server is the negative effect on\r\nthe performance of the mail server caused by the requirement to scan all messages. Also disadvantageous\r\nis that malware scanning on the mail server often requires significant modifications to the existing mail\r\nserver configuration. However, this option provides a number of advantages:\r\n\r\n- Can scan email in both directions (inbound and outbound)\r\n\r\n- Can be centrally managed to ensure compliance with the organization’s security policy and that\r\nupdates are applied regularly\r\n\r\n- Offers protection to internal users once malware is on the organization’s internal network.\r\nScanning for malware at the mail server has a number of weaknesses:\r\n\r\n- May require significant  modification of the existing mail server configuration (less true for most newer mail servers)\r\n\r\n- Cannot scan encrypted emails\r\n\r\n- May require more powerful (expensive) servers to handle the load of a large organization.\r\n\r\n- Can detect only those threats that have been identified; offers little protection against zero-day\r\n\r\n  exploits.\r\n  When considering mail server-based malware scanners, look for the following qualities:\r\n\r\n- Detects and cleans all types of malware typically carried by email (e.g., viruses, worms, Trojan  horses, malicious mobile code, spyware)\r\n\r\n- Provides heuristic scanning (provides some protection from new and unknown malware)\r\n\r\n- Provides content filtering \r\n\r\n- Incorporates mechanisms to help prevent email from circumventing the system\r\n\r\n- Provides ease of management\r\n\r\n- Provides automated downloading and installation of updates\r\n\r\n- Provides frequent updates (critical)\r\n\r\n- Can identify and apply rules to different types of content\r\n\r\n- Provides a robust and configurable alert mechanism\r\n\r\n- Provides detailed logging capabilities\r\n\r\nScanning on Client Hosts\r\n\r\nMalware scanners can also be located on client hosts (see Figure 6.3). This type of malware scanner is\r\ninstalled on user workstations and mobile devices, such as personal digital assistants (PDA). Incoming\r\nemails are scanned as they are opened by the user, and outbound emails are checked as the user attempts\r\nto send them. The primary advantage of this type of configuration is that scanning is distributed across\r\nmany hosts and therefore has minimal effect on the performance of each individual host. Also, if a client\r\nmachine becomes infected with malware, this layer of protection might stop the malware from spreading\r\nto the mail server and other mail clients.\r\nThe greatest challenge of implementing malware scanning on user workstations is the difficulty in\r\nmanaging and regularly updating the distributed malware scanners. However, enterprise-level solutions\r\nfor malware scanning provide a means of central administration of malware scanners on individual hosts.\r\nAnother weakness is that to the degree that users have control of the malware scanner, end users may\r\ndisable some or all of its functionality (whether accidentally or intentionally). Enterprise solutions offer\r\nthe capability to lock down some or all of the clients’ scanners’ functionality to ensure they are\r\nconfigured correctly.\r\n\r\nContent Filtering\r\n\r\nContent filtering works in a similar manner to malware scanning at the firewall or mail server except that\r\nit is looking for emails containing undesirable content other than malware, such as spam or emails\r\ncontaining inappropriate language. When implementing file-type restrictions and malware scanning, only\r\na certain level of security is provided. The contents of an email message or its attachments could prove\r\nmuch more damaging to an organization than a virus or rogue executable. For this case, some sort of\r\ncontent filtering mechanism should be employed.\r\nImplementing Content Filters\r\n\r\nFor maximum effectiveness, content filtering should be performed on all incoming and outgoing\r\nmessages and conducted in the same locations as malware scanning—on the firewall/mail relay/mail\r\ngateway, mail servers, and end users’ hosts. In fact, many products are available for popular messaging\r\nsystems that incorporate content filtering, malware scanning, and file-type restriction.\r\nIncorporation of these features into one product can reduce the administration of security controls.\r\n\r\nIn general, rules are defined to forward, quarantine, park, clean, block, or delete any data passing through\r\nthe server depending upon the results of the scan. Typical items that would be caught by the filter and\r\npossible actions taken on them could be as follows:\r\n\r\n- Email that contains suspicious active content (e.g., ActiveX, JavaScript) is stripped of the active code\r\n  and forwarded to the recipient.\r\n\r\n- Spam email and phishing attempts may be deleted or tagged as suspicious.\r\n\r\n- Extra-large files might be held for delivery during off-peak hours.\r\n\r\nAnother key feature of content filtering packages is the scanning of outbound data. A lexical analysis can\r\nbe performed that scans email messages for words and phrases that might be viewed as inappropriate for\r\nuse in organizational email. The lexical analysis can also save possible litigation against an organization\r\nby preventing inappropriate content, including hoaxes and spam (see Section 6.3), from leaving the\r\norganization. In addition, a lexical analysis might include searches for key words and phrases indicating\r\nthat sensitive data is leaving the enterprise.\r\n\r\nOrganizations should also take steps to prevent email address spoofing, such as ensuring that external\r\nusers cannot send emails to internal users that have one of the organization’s email addresses as the\r\nspoofed sender. For example, a hypothetical company WidgetsRUs should block any incoming email\r\nwith a “from” address in the domain widgetsrus.com at its mail gateway. Attackers often spoof email\r\naddresses to make their malicious emails appear to be from internal users, because it can trick users into\r\ntrusting the emails. Checking digital signatures on emails is a way that users can detect some spoofing attempts.\r\n\r\nfore implementing any filtering solution, it is imperative to determine how the existing network and\r\napplications actually work. This entails running network analyzers (sniffers); analyzing router, firewall,\r\nand server log files; and interviewing all appropriate system and network administrators. It is also\r\nimperative to analyze the existing organization information system security policy, or draft one if one\r\ndoes not exist. Clearly defined security policies are critical to translating the organization’s security goals\r\ninto filter rules. Great care must be taken in crafting the rules because an incorrectly configured filter\r\nmay fail to filter inappropriate content or may accidentally filter appropriate content. These steps will\r\n\r\nmake it easier to choose the appropriate filtering software and determine the types of rules that need to be\r\nconfigured.\r\n\r\nAnother effective way to decrease the number of unwanted messages reaching mail servers is using\r\nLightweight Directory Access Protocol (LDAP) lookup on a mail gateway or firewall as a filtering\r\nmechanism. LDAP lookup allows the gateway or firewall to query the organization’s user directory\r\ndirectly for user information. When an email is received by the gateway or firewall, it contacts the user\r\ndirectory to see if the email is addressed to a user that actually exists. If the user is not in the directory,\r\nthe email is rejected and does not reach the mail server. Much of the spam sent to a domain is generated\r\nusing a database of common usernames. Most of these addresses do not exist for a particular domain, but\r\nit is an easy method for spammers to get their messages to many users quickly. Using LDAP lookup\r\nprevents these messages from slowing the mail server.\r\n\r\nMany Internet service providers (ISP) and third-party companies offer malware scanning and content\r\nfiltering services, including spam filtering. These services can be helpful for organizations that wish to\r\nadd an extra layer of defense but do not want to implement or maintain the extra layer of protection\r\nthemselves. The services delete or tag messages before they reach an organization’s mail server,\r\ntherefore increasing its efficiency. Because these services may monitor emails for many organizations,\r\nthey can often identify new unwanted messages very quickly. Disadvantages of using such a service\r\ninclude the following:\r\n\r\n- Privacy. All of the organization’s incoming email is routed through the service provider’s servers\r\n  and scanned by them.\r\n\r\n- False Positives. The service provider’s filtering solution might automatically delete emails tagged as\r\n  spam or might not provide a way for administrators to check the validity of email tagging.\r\n\r\n- Availability. If the service becomes unavailable, the organization should be able to change the\r\n  routing of email to prevent delays in mail delivery.\r\n\r\nContent Filtering Issues\r\n\r\nAlthough email content filtering is critical to most organizations’ security posture, a number of legal\r\nimplications should be addressed before deployment. Content filtering needs to be backed up by a clearly\r\ndefined written security policy. The email policy should include an explicit statement that email will be\r\nmonitored for compliance, a description of any administrative or disciplinary actions that could result if\r\nthe policy is violated, and a requirement for employees to acknowledge reading and understanding the\r\npolicy. Although the policy should outline the organization’s thinking, expectations, and restrictions\r\nregarding security, due regard should also be given to employee and individual rights. For instance,\r\nunder some circumstances employees may have a right to privacy when it comes to their own\r\ncorrespondence; however, when representing their organization, the organization may be held legally\r\nresponsible for what they say or do. Without an established policy, such issues often lead to\r\nmisunderstanding and problems that can be difficult to resolve.\r\n\r\nUser Awareness\r\n\r\nIn addition to using anti-virus software and/or other malware scanning tools, as well as content filtering\r\nsoftware, organizations should educate users about the dangers posed by email-borne malware and\r\neffective ways of avoiding threats, including the following actions:\r\n\r\n- Never open attachments from unknown senders.\r\n\r\n- Never open attachments with suspicious or potentially harmful names or file extensions (e.g.,\r\n  attachment.txt.vbs, attachment.exe) from known or unknown senders.\r\n\r\n- Be suspicious of emails from known senders in which the subject line or content appears to be\r\n  inappropriate for the existing relationship (e.g., an email with the subject “I love you” from a\r\n  professional colleague) or generic subjects (e.g., “Look at this, it’s interesting”).\r\n\r\n- Scan all attachments with malware scanning software before opening, preferably by configuring the\r\n  scanning software to automatically perform this task.\r\n\r\n- Update the signature database of the malware scanning software at least on a daily basis or when\r\n  there is a malware outbreak.\r\n\r\n- Warn users about malware outbreaks and how to identify emails that might contain malware.\r\n\r\nUsers should also be aware of the dangers of phishing attacks and how to avoid them. The Federal Trade\r\nCommission (FTC) posted a consumer alert outlining steps that users should take:\r\n\r\n- Do not reply to email messages or popup ads asking for personal or financial information.\r\n\r\n- Do not trust phone numbers in emails or popup ads. Voice over IP technology can be used to register\r\n  a phone with any area code.\r\n\r\n- Do not email personal or financial information.\r\n\r\n- Review credit card and bank account statements regularly.\r\n\r\n- Be cautious about accessing untrusted Web sites, because some Web browser vulnerabilities can be\r\n  exploited simply by visiting a site. Users should also be cautious about opening any attachment or\r\n  downloading any file from untrusted emails or Web sites.\r\n\r\n- Forward phishing-related emails to spam@uce.gov and to the organization that is impersonated in the email.\r\n\r\n- Request a copy of your credit report from each of the three credit reporting agencies yearly: Equifax,\r\n  Transunion, and Experian. If an identity thief opens up accounts in your name, they will likely show\r\n  up on a credit report.");
                  
                  
                  
                     System.out.println("" +  SESC.getPEFM());
                     System.out.println();
                     System.out.println("************************************************************************************************" );
                     System.out.println();
                     System.out.println( "TO CONTINUE WITH NEXT SECURING-EMAIL-SERVERS-AND-CONTENT CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 10");
                     System.out.println();
                     System.out.println("************************************************************************************************" );   
                  
                  }
                  
                  else
                  
                     if ( menuSelect == 3 )
                     
                     {
                        System.out.println();
                        System.out.println();
                        System.out.println("BLOCKING-SPAM-SENDING-SERVERS: ");
                        System.out.println();  
                     
                        SESC.setBSSS("Blocking Spam-Sending Servers\r\n\r\nRegardless of the communication medium, there are always entities that attempt to exploit any means of\r\ncommunication to publicize their ideas or products. Email is no exception. The most common terms for\r\nthese messages are unsolicited commercial email (UCE), which is better known as spam. Most email\r\nusers receive spam on a daily basis. Because email is largely unregulated, system administrators should\r\npolice email traffic that traverses the servers they operate to reduce the amount of spam that reaches users.\r\nAn added benefit of implementing server-based spam control is that it will reduce mailbox sizes, which in\r\nturn reduces server storage requirements.\r\n\r\nTo control spam messages, administrators must address the following three concerns:\r\n\r\n- Ensure that spam cannot be sent from the mail servers they control \r\n\r\n.- Implement spam filtering for inbound messages\r\n\r\n.- Block messages from known spam-sending servers—the topic of this section.\r\n\r\nBecause the Internet has no centralized policing authority, non-profit organizations and commercial\r\ncompanies have created lists of mail servers that have been identified as being used to send unsolicited\r\nemail messages. These lists are often referred to as open relay blacklists (ORB) or DNS blacklists\r\n(DNSBL). Many popular mail server applications can be configured to query multiple ORBs and reject\r\nmessages originating from the listed mail servers. These lists are updated on a daily basis; therefore,\r\nusing them can drastically reduce spam message delivery. Additionally, most mail servers can be\r\nconfigured to reject messages from an explicitly defined set of domains.\r\nORB spam control is not foolproof. Open relays are connected and disconnected regularly.");
                     
                        System.out.println("" +  SESC.getBSSS());    
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                        System.out.println();
                        System.out.println( "TO CONTINUE WITH NEXT SECURING-EMAIL-SERVERS-AND-CONTENT CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 10");
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                     
                     }
                     
                     else
                     
                        if ( menuSelect == 4)
                        
                        {
                           System.out.println();
                           System.out.println("AUTHENTICATED-MAIL-RELAY: ");
                           System.out.println();
                        
                           SESC.setAMR("Authenticated Mail Relay\r\n\r\nAs mentioned previously, configuring mail relay authentication decreases the likelihood of someone\r\nusing a particular mail server to send spam. An added benefit of implementing authenticated relay is\r\nincreased security and usability.\r\n\r\nTwo methods are available for controlling mail relay. The first is to control the subnet or domain from\r\nwhich messages are being sent. This method is effective if the perimeter of the messaging system resides\r\nwithin known address ranges. However, if remote users have hosts with different address ranges, this\r\nmethod is not useful. To accommodate remote users, a more robust configuration is needed.\r\n\r\nThe second method is to require users to authenticate themselves before sending any messages. This is\r\ncommonly referred to as authenticated relay, or SMTP AUTH, which is the SMTP extension that supports\r\nuser authentication. Unfortunately, the default configuration of most mail servers does not implement\r\nauthenticated relay; therefore, mail server administrators must configure the server appropriately.\r\nRequiring authenticated relay is one of the least used but most powerful security features of mail servers.\r\n(Refer to manufacturer documentation for configuring SMTP AUTH.)\r\n\r\nMail server administrators must use caution if choosing to have an authenticated relay. An improperly\r\nconfigured mail server could be exploited and used to send or relay spam. If the mail server is found to\r\nbe an open relay, it might be put on a blacklist. Any organizations\r\nsubscribing to and using these blacklists will not be able to receive any email from a blacklisted server,\r\nwhether the messages are spam or valid emails.\r\n\r\nIf a mail server administrator learns that one of his or her mail servers is on a blacklist, the administrator\r\nwill have to fix the open relay problem and perform testing to ensure the server is no longer relaying. The\r\nadministrator then needs to determine which blacklists the server is on and check with each blacklist\r\nmaintainer to get instructions on how to remove the server from the lists. Until the server has been\r\nremoved from all blacklists and the updated blacklists have been propagated to their subscribers,\r\noutbound email from the organization may not reach all of its recipients.");
                        
                           System.out.println("" + SESC.getAMR());      
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                           System.out.println();
                           System.out.println( "TO CONTINUE WITH NEXT SECURING-EMAIL-SERVERS-AND-CONTENT CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 10");
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                        
                        }
                        
                        else
                        
                           if ( menuSelect == 5)
                           
                           {
                              System.out.println();         
                              System.out.println();
                              System.out.println(" SECURE-ACCESS:"); 
                              System.out.println();     
                           
                           
                              SESC.setSAC("Like many Internet protocols, most of these protocols did not initially incorporate any form of encryption or cryptographic\r\nauthentication. These deficits posed three problems for email users. First, for users sending messages,\r\nthe contents could be intercepted and read at any host on the path between the sender and recipient or\r\neven forged or modified. An apt paradigm from “regular” mail would be a postcard. Any person who\r\nhandles the postcard could read the message on the back. Second, the recipients could not verify that\r\nmessages were not modified by others during transit or actually originated by the sender. Third, rather\r\nthan supplying non-reusable authentication information, a user accessing a mailbox would send a\r\npassword over the network in the clear, which could be easily observed and reused by an attacker.\r\nUnfortunately, in most default configurations, mail clients are set up to send the user’s password in the\r\nclear, allowing it to be intercepted by other computers on the local network segment of the client or any\r\nhost responsible for forwarding the password to the mail server.\r\n\r\nThe first two problems, which discussed ways to protect messages. The third\r\nproblem can be resolved by applying the same method normally used to secure World Wide Web\r\n(WWW) traffic – the Transport Layer Security (TLS) protocol.\r\n\r\nTLS is similar to the Secure Sockets Layer (SSL) protocol, upon which it is based, and can be used in\r\ncombination with POP, IMAP, and SMTP to encrypt communication between mail clients and servers.\r\nRFC 2595 defines how to use TLS to combat communications eavesdropping, to implement secure\r\nmailbox access and to further strengthen SMTP MTAs that incorporate SMTP AUTH. shows\r\na sample configuration that enables TLS support for newer versions of sendmail.");
                           
                           
                              System.out.println("" + SESC.getSAC());
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                              System.out.println();
                              System.out.println( "TO CONTINUE WITH NEXT SECURING-EMAIL-SERVERS-AND-CONTENT CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 10");
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                           
                           }
                           
                           else
                           
                              if ( menuSelect == 6)
                              
                              {
                                 System.out.println();         
                                 System.out.println();
                                 System.out.println("ENABLING-WEB-ACCESS: "); 
                                 System.out.println();     
                              
                              
                                 SESC.setWAC("Increasingly, organizations are providing Web browser-based access to their messaging systems.\r\n\r\nEnabling this type of access could introduce security issues at both the client and server.\r\nAlthough Web site security is outside the scope of this document, there are several key concepts that\r\nshould be followed:\r\n\r\n- Avoid placing the Web server on the same machine as the mail server.\r\n\r\n- The authentication mechanism of the Web front-end should employ encryption.\r\n\r\n- The Web server should use SSL/TLS to encrypt all communications with clients.\r\n\r\n- As with any public server, the Web server should be hardened before connecting it to the network.\r\n\r\nFor some organizations, the processing requirements of dedicating a Web server to SSL/TLS\r\ncommunication may not be possible to accommodate. In cases such as this, the initial authentication\r\nshould be encrypted.\r\n\r\nSome organizations choose to use hardware appliances for their Web access solution. These appliances\r\nnot only provide secure Web-based access to mail servers, but they also provide firewall, content filtering,\r\nand malware protection capabilities. The appliances typically are easier and faster to install and maintain\r\nthan creating Web servers, and they often use hardened operating systems with all non-essential\r\ncomponents disabled or removed, which limits the possible vulnerabilities the appliances might have.\r\nSome appliances offer additional capabilities, such as offering administrators granular control over user\r\ngroups and access, performing SSL encryption for sessions, and terminating user sessions automatically after a period of inactivity. Appliances are available that support the most commonly used Web-based\r\nmail systems.\r\n\r\nClient security issues exist that also need to be considered before an organization approves the\r\ndeployment of Web access to email. ");
                              
                              
                                 System.out.println(" ENABLING WEB ACCESS           = " + SESC.getWAC());
                                 System.out.println();
                                 System.out.println("************************************************************************************************" );
                                 System.out.println();
                                 System.out.println( "TO CONTINUE WITH NEXT SECURING-EMAIL-SERVERS-AND-CONTENT PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 10");
                                 System.out.println();
                                 System.out.println("************************************************************************************************" );
                              
                              }
                              
                              else
                              
                                 if ( menuSelect == 7)
                                 
                                 {
                                    System.out.println();         
                                    System.out.println();
                                    System.out.println("CHECKLIST-FOR-ECURING-MAIL-SERVERS-AND-CONTENT: "); 
                                    System.out.println();
                                    SESC.setCSMC("Harden the mail server application\r\n\r\n- Install the mail server software on a dedicated host (if Web-based mail access is\r\n  desired, install the mail server software on a different host from the Web server)\r\n\r\n- Apply any patches or upgrades to correct for known vulnerabilities\r\n\r\n- Create a dedicated physical disk or logical partition (separate from operating\r\n\r\n- system and mail server application) for mailboxes, or host the mailboxes on a\r\n  separate server\r\n\r\n- Remove or disable all services installed by the mail server application but not\r\n  required (e.g., Web-based mail, FTP, remote administration)\r\n\r\n- Remove or disable all unneeded default login accounts created by the mail\r\n  server installation\r\n\r\n- Remove all manufacturer documentation from server\r\n\r\n- Remove any example or test files from server\r\n\r\n- Apply appropriate security template or hardening script to the server\r\n\r\n- Reconfigure SMTP, POP and IMAP service banners (and others as required)\r\n  NOT to report mail server and operating system type and version\r\n\r\n- Disable dangerous or unnecessary mail commands (e.g., VRFY and EXPN)\r\n  Configure operating system and mail server access controls\r\n\r\n- Limit the access of the mail server application to a subset of computational resources\r\n\r\n- Limit the access of users through additional access controls enforced by the mail\r\n  server, where more detailed levels of access control are required\r\n\r\n- Configure the mail server application to execute only under a unique individual\r\n  user and group identity with restrictive access controls\r\n\r\n- Ensure the mail server is not running with root or system/administrator privileges\r\n\r\n- Configure the host operating system so that the mail server can write log files but\r\n  not read them\r\n\r\n- Configure the host operating system so that temporary files created by the mail\r\n  server application are restricted to a specified and appropriately protected\r\n  subdirectory\r\n\r\n- Configure the host operating system so that access to any temporary files\r\n  created by the mail server application is limited to the mail server processes that\r\n  created these files\r\n\r\n- Ensure that the mail server cannot save files outside of the specified files\r\n  structure dedicated to the mail server\r\n\r\n- Configure the mail server to run in a chroot jail on Linux and Unix hosts\r\n\r\n- Install users’ mailboxes on a different server (preferred), hard drive, or logical\r\n  partition than the operating system and mail server application\r\n\r\nConfigure the mail server application so it cannot consume all available space on\r\nits hard drives or partitions\r\n\r\n- Limit the size of attachments that are allowed\r\n\r\n- Ensure log files are stored in a location that is sized appropriately\r\n- Protect email from malware\r\n\r\n- Determine which types of attachments to allow\r\n  Consider restricting the maximum acceptable size for attachments\r\n\r\n- Determine if having access to personal email accounts from organizational\r\n  computers is appropriate\r\n\r\n- Determine which types of active content should be permitted within email\r\n  messages\r\n\r\n- Implement centralized malware scanning (on the firewall, mail relay, mail\r\n  gateway, and/or mail server)\r\n\r\n- Install malware scanners on all client hosts\r\n\r\n- Implement centralized content filtering\r\n\r\n- Configure content filtering to block or tag suspicious messages (e.g., phishing,\r\n  spam)\r\n\r\n- Configure content filtering to strip suspicious active content from messages\r\n  Configure lexical analysis if required\r\n\r\n- Take steps to prevent address spoofing, such as blocking emails from external\r\n  locations using internal “From” addresses\r\n\r\n- Create a security policy that addresses content filtering\r\n\r\n- Have the security policy reviewed by appropriate legal, privacy, and human\r\n  resources authorities\r\n\r\n- Add a legal disclaimer to emails, if required\r\n\r\n- Educate users on the dangers of malware and how to minimize those dangers\r\n  Notify users when an outbreak occurs\r\n\r\n- Block spam-sending servers\r\n\r\n- Configure mail gateways or firewalls to use LDAP lookup to confirm the\r\n  existence of email recipients\r\n\r\n- Configure mail server to block email from open relay blacklists or DNS blacklists,\r\n  if required\r\n\r\n- Configure mail server to block email from specific domains, if required\r\n  Use authenticated mail relay\r\n\r\n- Configure authenticated mail relay on the server\r\n\r\n- Secure access to the mail server\r\n\r\n- Configure mail server to use encrypted authentication\r\n\r\n- Enable Web access to email\r\n\r\n- Configure mail server to support Web access only via SSL/TLS and only if such\r\n  access is deemed necessary. ");
                                 
                                 
                                    System.out.println("" + SESC.getCSMC());
                                    System.out.println();
                                    System.out.println("************************************************************************************************" );
                                    System.out.println();
                                    System.out.println( "TO CONTINUE WITH NEXT SECURING-EMAIL-SERVERS-AND-CONTENT CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 10");
                                    System.out.println();
                                    System.out.println("************************************************************************************************" );
                                 
                                 }
                                 
                                 
                                 else
                                 
                                    System.out.println();
               System.out.println   ("HERE ARE EMAIL-ISOLATION-FRAMEWORK MAIN MENU CATEGORIES LIST: ");
               System.out.println();
               System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
               System.out.println();
               System.out.println   ("2.  EMAIL STANDARDS ."); 
               System.out.println();
               System.out.println   ("3.  EMAIL SECURITY THREATS."); 
               System.out.println();
               System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
               System.out.println();
               System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
               System.out.println();
               System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
               System.out.println();
               System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
               System.out.println();
               System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
               System.out.println();
               System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
               System.out.println();
               System.out.println   ("12. SECURING EMAIL CLIENTS."); 
               System.out.println();
               System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
               System.out.println();
               System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
               System.out.println();
               System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
            
               menuSelection = keyboard.nextInt();
            
               while (menuSelection < 1 || menuSelection > 17) 
               
               {
               
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();  
                  System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("HERE IS THE VALID LIST OF EMAIL-ISOLATION MAIN MENU CATEGORIES: ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
                  System.out.println();
                  System.out.println   ("2.  EMAIL STANDARDS ."); 
                  System.out.println();
                  System.out.println   ("3.  EMAIL SECURITY THREATS."); 
                  System.out.println();
                  System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
                  System.out.println();
                  System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
                  System.out.println();
                  System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
                  System.out.println();
                  System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
                  System.out.println();
                  System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
                  System.out.println();
                  System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
                  System.out.println();
                  System.out.println   ("12. SECURING EMAIL CLIENTS."); 
                  System.out.println();
                  System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
                  System.out.println();
                  System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
                  System.out.println();
                  System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
               
               
               
                  menuSelection = keyboard.nextInt();
               
               } 
            
               break;
         
            case 11:
            
               EmailIsolationSetter ISNI;
               ISNI = new EmailIsolationSetter();
            
            
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println("YOU SELECTED IMPLEMENTING-SECURE-NETWORK-INFRASTRUCTURE CATEGORY FROM EMAIL-ISOLATION MAIN MENU ");
               System.out.println();
               System.out.println("PLEASE SEE BELOW IMPLEMENTING-SECURE-NETWORK-INFRASTRUCTURE CATEGORIES: ");
               System.out.println(); 
               System.out.println("1.  NETWORK COMPOSITION AND STRUCTURE.");
               System.out.println();
               System.out.println("2.  NETWORK ELEMENT CONFIGURATION.");
               System.out.println();
               System.out.println("3.  CHECKLIST FOR IMPLEMENTING A SECURE NETWORK INFRASTRUCTURE.");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print(" ENTER YOUR CHOICE IMPLEMENTING-SECURE-NETWORK-INFRASTRUCTURE CATEGORIES (1 to 3): ");
            
            
               menuSelect = keyboard.nextInt();
            
               while (menuSelect < 1 || menuSelect > 3)
               
               {
               
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println("THIS IS INVALID CHOICE FOR IMPLEMENTING-SECURE-NETWORK-INFRASTRUCTURE SELECTION "); 
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW VALID IMPLEMENTING-SECURE-NETWORK-INFRASTRUCTURE SELECTIONS:");
                  System.out.println();
                  System.out.println("1.  NETWORK COMPOSITION AND STRUCTURE.");
                  System.out.println();
                  System.out.println("2.  NETWORK ELEMENT CONFIGURATION.");
                  System.out.println();
                  System.out.println("3.  CHECKLIST FOR IMPLEMENTING A SECURE NETWORK INFRASTRUCTURE.");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER YOUR CHOICE IMPLEMENTING-SECURE-NETWORK-INFRASTRUCTURE CATEGORIES (1 to 3): ");
               
               
               
               
                  menuSelect = keyboard.nextInt();
               
               }
            
               /*System.out.println();
               System.out.println(" NOTE: There are eight performance attributes, or currencies, to be considered when evaluating whether a EMAIL-ISOLATION network can deliver on its full potential.".toUpperCase());
               System.out.println();                
               System.out.println(" NOTE:  Without all eight of these currencies, you don’t have a true EMAIL-ISOLATION network. With them, you have a powerful, game-changing platform for innovation .".toUpperCase());
               System.out.println();
               */ 
            
               if ( menuSelect == 1)
               
               {          
                  System.out.println();
                  System.out.println("NETWORK-COMPOSITION-AND-STRUCTURE: ");
                  System.out.println();
               
               
                  ISNI.setNCAS           (". ");
               
               
                  System.out.println               ("" +  ISNI.getNCAS());                  System.out.println();          
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println( "TO CONTINUE WITH NEXT IMPLEMENTING-SECURE-NETWORK-INFRASTRUCTURE CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU  CHOICE # 1");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
               
               }
               
               else
               
                  if ( menuSelect == 2)
                  
                  {
                     System.out.println();
                     System.out.println();
                     System.out.println("PLEASE SEE BELOW NETWORK-ELEMENT-CONFIGURATION: ");
                     System.out.println();
                  
                     ISNI.setNEC (". ");
                  
                  
                  
                     System.out.println(" NETWORK ELEMENT CONFIGURATION             = " +  ISNI.getNEC());
                     System.out.println();
                     System.out.println("************************************************************************************************" );
                     System.out.println();
                     System.out.println( "TO CONTINUE WITH NEXT IMPLEMENTING-SECURE-NETWORK-INFRASTRUCTURE CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                     System.out.println();
                     System.out.println("************************************************************************************************" );   
                  
                  }
                  
                  else
                  
                     if ( menuSelect == 3 )
                     
                     {
                        System.out.println();
                        System.out.println();
                        System.out.println("PLEASE SEE BELOW CHECKLIST-FOR-IMPLEMENTING-A-SECURE-NETWORK-INFRASTRUCTURE: ");
                        System.out.println();  
                     
                        ISNI.setCISN(". ");
                     
                        System.out.println(" CHECKLIST FOR IMPLEMENTING A SECURE NETWORK INFRASTRUCTURE      = " +  ISNI.getCISN());    
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                        System.out.println();
                        System.out.println( "TO CONTINUE WITH NEXT IMPLEMENTING-SECURE-NETWORK-INFRASTRUCTURE CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                     
                     }
                     
                     
                     else
                     
                        System.out.println();
               System.out.println   ("HERE ARE EMAIL-ISOLATION-FRAMEWORK MAIN MENU CATEGORIES LIST: ");
               System.out.println();
               System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
               System.out.println();
               System.out.println   ("2.  EMAIL STANDARDS ."); 
               System.out.println();
               System.out.println   ("3.  EMAIL SECURITY THREATS."); 
               System.out.println();
               System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
               System.out.println();
               System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
               System.out.println();
               System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
               System.out.println();
               System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
               System.out.println();
               System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
               System.out.println();
               System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
               System.out.println();
               System.out.println   ("12. SECURING EMAIL CLIENTS."); 
               System.out.println();
               System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
               System.out.println();
               System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
               System.out.println();
               System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
            
               menuSelection = keyboard.nextInt();
            
               while (menuSelection < 1 || menuSelection > 17) 
               
               {
               
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();  
                  System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("HERE IS THE VALID LIST OF EMAIL-ISOLATION MAIN MENU CATEGORIES: ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
                  System.out.println();
                  System.out.println   ("2.  EMAIL STANDARDS ."); 
                  System.out.println();
                  System.out.println   ("3.  EMAIL SECURITY THREATS."); 
                  System.out.println();
                  System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
                  System.out.println();
                  System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
                  System.out.println();
                  System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
                  System.out.println();
                  System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
                  System.out.println();
                  System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
                  System.out.println();
                  System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
                  System.out.println();
                  System.out.println   ("12. SECURING EMAIL CLIENTS."); 
                  System.out.println();
                  System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
                  System.out.println();
                  System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
                  System.out.println();
                  System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
               
               
               
                  menuSelection = keyboard.nextInt();
               
               } 
            
               break;
         
            case 12:
            
               EmailIsolationSetter SEC;
               SEC = new EmailIsolationSetter();
            
            
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println("YOU SELECTED SECURING-EMAIL-CLIENTS CATEGORY FROM EMAIL-ISOLATION MAIN MENU ");
               System.out.println();
               System.out.println("PLEASE SEE BELOW SECURING-EMAIL-CLIENTS CATEGORIES: ");
               System.out.println(); 
               System.out.println("1.  INSTALLING CONFIGURATION CLIENT APPLICATIONS.");
               System.out.println();
               System.out.println("2.  SECURE MESSAGE COMPOSITION.");
               System.out.println();
               System.out.println("3.  PLUG-INS.");
               System.out.println();
               System.out.println("4.  ACCESSING WEB-BASED MAIL SYSTEMS.");
               System.out.println();
               System.out.println("5. CHECKLIST FORECURING MAIL CLIENTS.");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print(" ENTER YOUR CHOICE MALWARE-INCIDENT-RESPONSE CATEGORIES (1 to 5): ");
            
            
               menuSelect = keyboard.nextInt();
            
               while (menuSelect < 1 || menuSelect > 5)
               
               {
               
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println("THIS IS INVALID CHOICE FOR SECURING-EMAIL-CLIENTS SELECTION "); 
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW VALID SECURING-EMAIL-CLIENTS SELECTIONS:");
                  System.out.println();
                  System.out.println("1.  INSTALLING CONFIGURATION CLIENT APPLICATIONS.");
                  System.out.println();
                  System.out.println("2.  SECURE MESSAGE COMPOSITION.");
                  System.out.println();
                  System.out.println("3.  PLUG-INS.");
                  System.out.println();
                  System.out.println("4.  ACCESSING WEB-BASED MAIL SYSTEMS.");
                  System.out.println();
                  System.out.println("5.  CHECKLIST FORECURING MAIL CLIENTS.");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print(" ENTER YOUR CHOICE MALWARE-INCIDENT-RESPONSE CATEGORIES (1 to 5): ");
               
               
               
               
                  menuSelect = keyboard.nextInt();
               
               }
            
               System.out.println();
               System.out.println(" NOTE: There are eight performance attributes, or currencies, to be considered when evaluating whether a EMAIL-ISOLATION network can deliver on its full potential.".toUpperCase());
               System.out.println();                
               System.out.println(" NOTE:  Without all eight of these currencies, you don’t have a true EMAIL-ISOLATION network. With them, you have a powerful, game-changing platform for innovation .".toUpperCase());
               System.out.println(); 
            
               if ( menuSelect == 1)
               
               {          
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW INSTALLING-CONFIGURATION-CLIENT-APPLICATIONS: ");
                  System.out.println();
               
               
                  SEC.setICCA           (". ");
               
               
                  System.out.println               (" INSTALLING CONFIGURATION CLIENT APPLICATIONS                = " +  SEC.getICCA());
                  System.out.println();          
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println( "TO CONTINUE WITH NEXT SECURING-EMAIL-CLIENTS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU  CHOICE # 1");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
               
               }
               
               else
               
                  if ( menuSelect == 2)
                  
                  {
                     System.out.println();
                     System.out.println();
                     System.out.println("PLEASE SEE BELOW SECURE-MESSAGE-COMPOSITION");
                     System.out.println();
                  
                     SEC.setSMC (". ");
                  
                  
                  
                     System.out.println(" SECURE MESSAGE COMPOSITION             = " +  SEC.getSMC());
                     System.out.println();
                     System.out.println("************************************************************************************************" );
                     System.out.println();
                     System.out.println( "TO CONTINUE WITH NEXT SECURING-EMAIL-CLIENTS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                     System.out.println();
                     System.out.println("************************************************************************************************" );   
                  
                  }
                  
                  else
                  
                     if ( menuSelect == 3 )
                     
                     {
                        System.out.println();
                        System.out.println();
                        System.out.println("PLEASE SEE BELOW PLUG-INS: ");
                        System.out.println();  
                     
                        SEC.setPI(". ");
                     
                        System.out.println(" PLUG-INS      = " +  SEC.getPI());    
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                        System.out.println();
                        System.out.println( "TO CONTINUE WITH NEXT SECURING-EMAIL-CLIENTS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                     
                     }
                     
                     else
                     
                        if ( menuSelect == 4)
                        
                        {
                           System.out.println();
                           System.out.println("PLEASE SEE BELOW ACCESSING-WEB-BASED-MAIL-SYSTEMS: ");
                           System.out.println();
                        
                           SEC.setAWBMS(". ");
                        
                           System.out.println(" ACCESSING WEB-BASED MAIL SYSTEMS    = " + SEC.getAWBMS());      
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                           System.out.println();
                           System.out.println( "TO CONTINUE WITH NEXT SECURING-EMAIL-CLIENTS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                        
                        }
                        
                        else
                        
                           if ( menuSelect == 5)
                           
                           {
                              System.out.println();         
                              System.out.println();
                              System.out.println("PLEASE SEE BELOW CHECKLIST-FOR-SECURING-MAIL-CLIENTS:"); 
                              System.out.println();     
                           
                           
                              SEC.setCSFMC(".");
                           
                           
                              System.out.println(" CHECKLIST FORECURING MAIL CLIENTS           = " + SEC.getCSFMC());
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                              System.out.println();
                              System.out.println( "TO CONTINUE WITH NEXTSECURING-EMAIL-CLIENTS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                           
                           }
                           
                           
                           else
                           
                              System.out.println();
               System.out.println   ("HERE ARE EMAIL-ISOLATION-FRAMEWORK MAIN MENU CATEGORIES LIST: ");
               System.out.println();
               System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
               System.out.println();
               System.out.println   ("2.  EMAIL STANDARDS ."); 
               System.out.println();
               System.out.println   ("3.  EMAIL SECURITY THREATS."); 
               System.out.println();
               System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
               System.out.println();
               System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
               System.out.println();
               System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
               System.out.println();
               System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
               System.out.println();
               System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
               System.out.println();
               System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
               System.out.println();
               System.out.println   ("12. SECURING EMAIL CLIENTS."); 
               System.out.println();
               System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
               System.out.println();
               System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
               System.out.println();
               System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
            
               menuSelection = keyboard.nextInt();
            
               while (menuSelection < 1 || menuSelection > 17) 
               
               {
               
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();  
                  System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("HERE IS THE VALID LIST OF EMAIL-ISOLATION MAIN MENU CATEGORIES: ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
                  System.out.println();
                  System.out.println   ("2.  EMAIL STANDARDS ."); 
                  System.out.println();
                  System.out.println   ("3.  EMAIL SECURITY THREATS."); 
                  System.out.println();
                  System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
                  System.out.println();
                  System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
                  System.out.println();
                  System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
                  System.out.println();
                  System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
                  System.out.println();
                  System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
                  System.out.println();
                  System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
                  System.out.println();
                  System.out.println   ("12. SECURING EMAIL CLIENTS."); 
                  System.out.println();
                  System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
                  System.out.println();
                  System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
                  System.out.println();
                  System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
               
               
               
                  menuSelection = keyboard.nextInt();
               
               } 
            
            
               break;
         
            case 13:
            
               EmailIsolationSetter AEMS;
               AEMS = new EmailIsolationSetter();
            
            
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println("YOU SELECTED ADMINISTERING-THE-EMAIL-SERVERS CATEGORY FROM EMAIL-ISOLATION MAIN MENU ");
               System.out.println();
               System.out.println("PLEASE SEE BELOW ADMINISTERING-THE-EMAIL-SERVERS CATEGORIES: ");
               System.out.println(); 
               System.out.println("1. LOGGING .");
               System.out.println();
               System.out.println("2. BACKING UP MAIL-SERVERS .");
               System.out.println();
               System.out.println("3. RECOVERING FROM SECURITY COMPROMISE.");
               System.out.println();
               System.out.println("4.  SECURITY TESTING MAIL-SERVERS.");
               System.out.println();
               System.out.println("5.  REMOTELY ADMINISTRING A MAIL-SERVER.");
               System.out.println();
               System.out.println("6.  CHECKLIST FOR ADMINISTRING THE MAIL-SERVER.");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print(" ENTER YOUR CHOICE ADMINISTERING-THE-EMAIL-SERVERS CATEGORIES (1 to 6): ");
            
            
               menuSelect = keyboard.nextInt();
            
               while (menuSelect < 1 || menuSelect > 6)
               
               {
               
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println("THIS IS INVALID CHOICE FOR ADMINISTERING-THE-EMAIL-SERVERS SELECTION "); 
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW VALID ADMINISTERING-THE-EMAIL-SERVERS SELECTIONS:");
                  System.out.println();
                  System.out.println("1. LOGGING.");
                  System.out.println();
                  System.out.println("2. BACKING UP MAIL-SERVERS.");
                  System.out.println();
                  System.out.println("3. RECOVERING FROM SECURITY COMPROMISE.");
                  System.out.println();
                  System.out.println("4.  SECURITY TESTING MAIL0-SERVERS.");
                  System.out.println();
                  System.out.println("5.  REMOTELY ADMINISTRING A MAIL-SERVER.");
                  System.out.println();
                  System.out.println("6.  CHECKLIST FOR ADMINISTRING THE MAIL-SERVER.");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print(" ENTER YOUR CHOICE ADMINISTERING-THE-EMAIL-SERVERS CATEGORIES (1 to 6): ");
               
               
               
               
                  menuSelect = keyboard.nextInt();
               
               }
            
               System.out.println();
               System.out.println(" NOTE: There are eight performance attributes, or currencies, to be considered when evaluating whether a EMAIL-ISOLATION network can deliver on its full potential.".toUpperCase());
               System.out.println();                
               System.out.println(" NOTE:  Without all eight of these currencies, you don’t have a true EMAIL-ISOLATION network. With them, you have a powerful, game-changing platform for innovation .".toUpperCase());
               System.out.println(); 
            
               if ( menuSelect == 1)
               
               {          
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW LOGGING: ");
                  System.out.println();
               
               
                  AEMS.setLOG          (". ");
               
               
                  System.out.println               (" LOGGING                = " +  AEMS.getLOG());
                  System.out.println();          
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println( "TO CONTINUE WITH NEXT ADMINISTERING-THE-EMAIL-SERVERS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU  CHOICE # 1");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
               
               }
               
               else
               
                  if ( menuSelect == 2)
                  
                  {
                     System.out.println();
                     System.out.println();
                     System.out.println("PLEASE SEE BELOW BACKING UP MAIL-SERVERS: ");
                     System.out.println();
                  
                     AEMS.setBMAS (". ");
                  
                  
                  
                     System.out.println(" BACKING UP MAIL-SERVERS             = " +  AEMS.getBMAS());
                     System.out.println();
                     System.out.println("************************************************************************************************" );
                     System.out.println();
                     System.out.println( "TO CONTINUE WITH NEXT ADMINISTERING-THE-EMAIL-SERVERS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                     System.out.println();
                     System.out.println("************************************************************************************************" );   
                  
                  }
                  
                  else
                  
                     if ( menuSelect == 3 )
                     
                     {
                        System.out.println();
                        System.out.println();
                        System.out.println("PLEASE SEE BELOW RECOVERING0-FROM-SECURITY-COMPROMISE: ");
                        System.out.println();  
                     
                        AEMS.setRFSC(". ");
                     
                        System.out.println(" RECOVERING FROM SECURITY COMPROMISE      = " +  AEMS.getRFSC());    
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                        System.out.println();
                        System.out.println( "TO CONTINUE WITH NEXT ADMINISTERING-THE-EMAIL-SERVERS CATEGORY CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                     
                     }
                     
                     else
                     
                        if ( menuSelect == 4)
                        
                        {
                           System.out.println();
                           System.out.println("PLEASE SEE BELOW SECURITY-TESTING-MAIL-SERVERS: ");
                           System.out.println();
                        
                           AEMS.setSTMS(". ");
                        
                           System.out.println(" SECURITY TESTING MAIL-SERVERS.     = " + AEMS.getSTMS());      
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                           System.out.println();
                           System.out.println( "TO CONTINUE WITH NEXT ADMINISTERING-THE-EMAIL-SERVERS CATEGORY CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                        
                        }
                        
                        else
                        
                           if ( menuSelect == 5)
                           
                           {
                              System.out.println();         
                              System.out.println();
                              System.out.println("PLEASE SEE BELOW REMOTELY-ADMINISTRING0-A-MAIL-SERVER:"); 
                              System.out.println();     
                           
                           
                              AEMS.setRAMS(".");
                           
                           
                              System.out.println(" REMOTELY ADMINISTRING A MAIL-SERVER           = " + AEMS.getRAMS());
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                              System.out.println();
                              System.out.println( "TO CONTINUE WITH NEXT ADMINISTERING-THE-EMAIL-SERVERS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                           
                           }
                           
                           else
                           
                              if ( menuSelect == 6)
                              
                              {
                                 System.out.println();         
                                 System.out.println();
                                 System.out.println("PLEASE SEE BELOW CHECKLIST-FOR-ADMINISTRING-THE-MAIL-SERVER: "); 
                                 System.out.println();     
                              
                              
                                 AEMS.setCAMS(".");
                              
                              
                                 System.out.println(" MALWARE-INCIDENT LESSONS LEARNED           = " + AEMS.getCAMS());
                                 System.out.println();
                                 System.out.println("************************************************************************************************" );
                                 System.out.println();
                                 System.out.println( "TO CONTINUE WITH NEXT ADMINISTERING-THE-EMAIL-SERVERS CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                                 System.out.println();
                                 System.out.println("************************************************************************************************" );
                              
                              }
                              
                              
                              else
                              
                                 System.out.println();
               System.out.println   ("HERE ARE EMAIL-ISOLATION-FRAMEWORK MAIN MENU CATEGORIES LIST: ");
               System.out.println();
               System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
               System.out.println();
               System.out.println   ("2.  EMAIL STANDARDS ."); 
               System.out.println();
               System.out.println   ("3.  EMAIL SECURITY THREATS."); 
               System.out.println();
               System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
               System.out.println();
               System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
               System.out.println();
               System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
               System.out.println();
               System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
               System.out.println();
               System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
               System.out.println();
               System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
               System.out.println();
               System.out.println   ("12. SECURING EMAIL CLIENTS."); 
               System.out.println();
               System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN AND INDIVIDUAL MAIL MESSAGES.");
               System.out.println();
               System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
               System.out.println();
               System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
               System.out.println();
               System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
            
               menuSelection = keyboard.nextInt();
            
               while (menuSelection < 1 || menuSelection > 17) 
               
               {
               
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();  
                  System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("HERE IS THE VALID LIST OF EMAIL-ISOLATION MAIN MENU CATEGORIES: ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
                  System.out.println();
                  System.out.println   ("2.  EMAIL STANDARDS ."); 
                  System.out.println();
                  System.out.println   ("3.  EMAIL SECURITY THREATS."); 
                  System.out.println();
                  System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
                  System.out.println();
                  System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
                  System.out.println();
                  System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
                  System.out.println();
                  System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
                  System.out.println();
                  System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
                  System.out.println();
                  System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
                  System.out.println();
                  System.out.println   ("12. SECURING EMAIL CLIENTS."); 
                  System.out.println();
                  System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN AND INDIVIDUAL MAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
                  System.out.println();
                  System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
                  System.out.println();
                  System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
               
               
               
                  menuSelection = keyboard.nextInt();
               
               } 
            
               break;
         
            case 14:
            
               EmailIsolationSetter ASDIMM;
               ASDIMM = new EmailIsolationSetter();
            
            
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println("YOU SELECTED AUTHENTICATING-A-SENDING-DOMAIN-AND-INDIVIDUAL-MAIL-MESSAGES CATEGORY FROM EMAIL-ISOLATION MAIN MENU ");
               System.out.println();
               System.out.println("PLEASE SEE BELOW AUTHENTICATING-A-SENDING-DOMAIN-AND-INDIVIDUAL-MAIL-MESSAGES CATEGORIES: ");
               System.out.println(); 
               System.out.println("1.  INTRODUCTION.");
               System.out.println();
               System.out.println("2.  VISIBILITY TO END USERS.");
               System.out.println();
               System.out.println("3.  REQUIREMENTS FOR USING DOMAIN-BASED AUTHENTICATING TECHNIQUES FOR FEDERAL SYSTEMS.");
               System.out.println();
               System.out.println("4.  SENDERS POLICY FRAMEWORK (SPF).");
               System.out.println();
               System.out.println("5.  DOMAINS-KEYS IDENTIFIED MAIL (DKIM).");
               System.out.println();
               System.out.println("6.  DOMAIN-BASED AUTHENTICATION, REPORTING AND CONFORMANCE (DMARC).");
               System.out.println();
               System.out.println("7.  AUTHENTICATING MAIL MESSAGES WITH DIGITAL SIGNATURES.");
               System.out.println();
               System.out.println("8.  RECOMMENDATION SUMMARY.");
               System.out.println();
            
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print(" ENTER YOUR AUTHENTICATING-A-SENDING-DOMAIN-AND-INDIVIDUAL-MAIL-MESSAGES CHOICE (1 to 8): ");
            
            
               menuSelect = keyboard.nextInt();
            
               while (menuSelect < 1 || menuSelect > 8)
               
               {
               
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println("THIS IS INVALID CHOICE FOR AUTHENTICATING-A-SENDING-DOMAIN-AND-INDIVIDUAL-MAIL-MESSAGES SELECTION "); 
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW VALID AUTHENTICATING-A-SENDING-DOMAIN-AND-INDIVIDUAL-MAIL-MESSAGES SELECTIONS:");
                  System.out.println();
                  System.out.println("1.  INTRODUCTION.");
                  System.out.println();
                  System.out.println("2.  VISIBILITY TO END USERS.");
                  System.out.println();
                  System.out.println("3.  REQUIREMENTS FOR USING DOMAIN-BASED AUTHENTICATING TECHNIQUES FOR FEDERAL SYSTEMS.");
                  System.out.println();
                  System.out.println("4.  SENDERS POLICY FRAMEWORK (SPF).");
                  System.out.println();
                  System.out.println("5.  DOMAINS-KEYS IDENTIFIED MAIL (DKIM).");
                  System.out.println();
                  System.out.println("6.  DOMAIN-BASED AUTHENTICATION, REPORTING AND CONFORMANCE (DMARC).");
                  System.out.println();
                  System.out.println("7.  AUTHENTICATING MAIL MESSAGES WITH DIGITAL SIGNATURES.");
                  System.out.println();
                  System.out.println("8.  RECOMMENDATION SUMMARY.");
                  System.out.println();
               
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print(" ENTER YOUR AUTHENTICATING-A-SENDING-DOMAIN-AND-INDIVIDUAL-MAIL-MESSAGES CHOICE (1 to 8): ");
               
               
               
               
                  menuSelect = keyboard.nextInt();
               
               }
            
               System.out.println();
               System.out.println(" NOTE: There are eight performance attributes, or currencies, to be considered when evaluating whether a EMAIL-ISOLATION network can deliver on its full potential.".toUpperCase());
               System.out.println();                
               System.out.println(" NOTE:  Without all eight of these currencies, you don’t have a true EMAIL-ISOLATION network. With them, you have a powerful, game-changing platform for innovation .".toUpperCase());
               System.out.println(); 
            
               if ( menuSelect == 1)
               
               {          
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW INTRODUCTION: ");
                  System.out.println();
               
               
                  ASDIMM.setINTRO          (". ");
               
               
                  System.out.println               (" INTRODUCTION               = " +  ASDIMM.getINTRO());
                  System.out.println();          
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println( "TO CONTINUE WITH NEXT AUTHENTICATING-A-SENDING-DOMAIN-AND-INDIVIDUAL-MAIL-MESSAGES CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU  CHOICE # 1");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
               
               }
               
               else
               
                  if ( menuSelect == 2)
                  
                  {
                     System.out.println();
                     System.out.println();
                     System.out.println("PLEASE SEE BELOW VISIBILITY-TO-END-USERS: ");
                     System.out.println();
                  
                     ASDIMM.setVEU (". ");
                  
                  
                  
                     System.out.println(" VISIBILITY TO END USERS             = " +  ASDIMM.getVEU());
                     System.out.println();
                     System.out.println("************************************************************************************************" );
                     System.out.println();
                     System.out.println( "TO CONTINUE WITH NEXT AUTHENTICATING-A-SENDING-DOMAIN-AND-INDIVIDUAL-MAIL-MESSAGES CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                     System.out.println();
                     System.out.println("************************************************************************************************" );   
                  
                  }
                  
                  else
                  
                     if ( menuSelect == 3 )
                     
                     {
                        System.out.println();
                        System.out.println();
                        System.out.println("PLEASE SEE BELOW REQUIREMENTS-FOR-USING-DOMAIN-BASED-AUTHENTICATING-TECHNIQUES-FOR-FEDERAL-SYSTEMS: ");
                        System.out.println();  
                     
                        ASDIMM.setRUDBA(". ");
                     
                        System.out.println(" REQUIREMENTS FOR USING DOMAIN-BASED AUTHENTICATING TECHNIQUES FOR FEDERAL SYSTEMS      = " +  ASDIMM.getRUDBA());    
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                        System.out.println();
                        System.out.println( "TO CONTINUE WITH NEXT AUTHENTICATING-A-SENDING-DOMAIN-AND-INDIVIDUAL-MAIL-MESSAGES CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                     
                     }
                     
                     else
                     
                        if ( menuSelect == 4)
                        
                        {
                           System.out.println();
                           System.out.println("PLEASE SEE BELOW SENDERS-POLICY-FRAMEWORK (SPF): ");
                           System.out.println();
                        
                           ASDIMM.setSPF(". ");
                        
                           System.out.println(" SENDERS POLICY FRAMEWORK (SPF).     = " + ASDIMM.getSPF());      
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                           System.out.println();
                           System.out.println( "TO CONTINUE WITH NEXT AUTHENTICATING-A-SENDING-DOMAIN-AND-INDIVIDUAL-MAIL-MESSAGES CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                        
                        }
                        
                        else
                        
                           if ( menuSelect == 5)
                           
                           {
                              System.out.println();         
                              System.out.println();
                              System.out.println("PLEASE SEE BELOW DOMAINS-KEYS-IDENTIFIED-MAIL (DKIM):"); 
                              System.out.println();     
                           
                           
                              ASDIMM.setDKIM(".");
                           
                           
                              System.out.println(" DOMAINS-KEYS IDENTIFIED MAIL (DKIM)          = " + ASDIMM.getDKIM());
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                              System.out.println();
                              System.out.println( "TO CONTINUE WITH NEXT AUTHENTICATING-A-SENDING-DOMAIN-AND-INDIVIDUAL-MAIL-MESSAGES CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                           
                           }
                           
                           else
                           
                              if ( menuSelect == 6)
                              
                              {
                                 System.out.println();         
                                 System.out.println();
                                 System.out.println("PLEASE SEE BELOW DOMAIN-BASED-AUTHENTICATION-REPORTING-AND-CONFORMANCE (DMARC): "); 
                                 System.out.println();     
                              
                              
                                 ASDIMM.setDMARC(".");
                              
                              
                                 System.out.println(" DOMAIN-BASED AUTHENTICATION, REPORTING AND CONFORMANCE (DMARC)           = " + ASDIMM.getDMARC());
                                 System.out.println();
                                 System.out.println("************************************************************************************************" );
                                 System.out.println();
                                 System.out.println( "TO CONTINUE WITH NEXT AUTHENTICATING-A-SENDING-DOMAIN-AND-INDIVIDUAL-MAIL-MESSAGES CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                                 System.out.println();
                                 System.out.println("************************************************************************************************" );
                              
                              }
                              
                              else
                              
                                 if ( menuSelect == 7)
                                 
                                 {
                                    System.out.println();         
                                    System.out.println();
                                    System.out.println("PLEASE SEE BELOW AUTHENTICATING-MAIL-MESSAGES-WITH-DIGITAL-SIGNATURES:"); 
                                    System.out.println();     
                                 
                                 
                                    ASDIMM.setAMDS(".");
                                 
                                 
                                    System.out.println(" AUTHENTICATING MAIL MESSAGES WITH DIGITAL SIGNATURES           = " + ASDIMM.getAMDS());
                                    System.out.println();
                                    System.out.println("************************************************************************************************" );
                                    System.out.println();
                                    System.out.println( "TO CONTINUE WITH NEXT AUTHENTICATING-A-SENDING-DOMAIN-AND-INDIVIDUAL-MAIL-MESSAGES CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                                    System.out.println();
                                    System.out.println("************************************************************************************************" );
                                 
                                 }
                                 
                                 else
                                 
                                    if ( menuSelect == 8)
                                    
                                    {
                                       System.out.println();         
                                       System.out.println();
                                       System.out.println("PLEASE SEE BELOW RECOMMENDATION0-SUMMARY: "); 
                                       System.out.println();     
                                    
                                    
                                       ASDIMM.setRS(".");
                                    
                                    
                                       System.out.println(" RECOMMENDATION SUMMARY           = " + ASDIMM.getRS());
                                       System.out.println();
                                       System.out.println("************************************************************************************************" );
                                       System.out.println();
                                       System.out.println( "TO CONTINUE WITH NEXT AUTHENTICATING-A-SENDING-DOMAIN-AND-INDIVIDUAL-MAIL-MESSAGES CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                                       System.out.println();
                                       System.out.println("************************************************************************************************" );
                                    
                                    }
                                    
                                    else
                                    
                                       System.out.println();
               System.out.println   ("HERE ARE EMAIL-ISOLATION-FRAMEWORK MAIN MENU CATEGORIES LIST: ");
               System.out.println();
               System.out.println   ("1.  EMAIL ISOLATION ELEMENTS. "); 
               System.out.println();
               System.out.println   ("2.  EMAIL STANDARDS ."); 
               System.out.println();
               System.out.println   ("3.  EMAIL SECURITY THREATS."); 
               System.out.println();
               System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
               System.out.println();
               System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
               System.out.println();
               System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
               System.out.println();
               System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
               System.out.println();
               System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
               System.out.println();
               System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
               System.out.println();
               System.out.println   ("12. SECURING EMAIL CLIENTS."); 
               System.out.println();
               System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
               System.out.println();
               System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
               System.out.println();
               System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
            
               menuSelection = keyboard.nextInt();
            
               while (menuSelection < 1 || menuSelection > 17) 
               
               {
               
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();  
                  System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("HERE IS THE VALID LIST OF EMAIL-ISOLATION MAIN MENU CATEGORIES: ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
                  System.out.println();
                  System.out.println   ("2.  EMAIL STANDARDS ."); 
                  System.out.println();
                  System.out.println   ("3.  EMAIL SECURITY THREATS."); 
                  System.out.println();
                  System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
                  System.out.println();
                  System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
                  System.out.println();
                  System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
                  System.out.println();
                  System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
                  System.out.println();
                  System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
                  System.out.println();
                  System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
                  System.out.println();
                  System.out.println   ("12. SECURING EMAIL CLIENTS."); 
                  System.out.println();
                  System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
                  System.out.println();
                  System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
                  System.out.println();
                  System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
               
               
               
                  menuSelection = keyboard.nextInt();
               
               } 
            
               break;
         
            case 15:
            
               EmailIsolationSetter PEC;
               PEC = new EmailIsolationSetter();
            
            
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println("YOU SELECTED PROTECTING-EMAIL-CONFIDENTIALITY CATEGORY FROM EMAIL-ISOLATION MAIN MENU ");
               System.out.println();
               System.out.println("PLEASE SEE BELOW PROTECTING-EMAIL-CONFIDENTIALITY CATEGORIES: ");
               System.out.println(); 
               System.out.println("1.  INTRODUCTION.");
               System.out.println();
               System.out.println("2.  EMAIL TRANSMISSION SECURITY.");
               System.out.println();
               System.out.println("3.  EMAIL CONTENT SECURITY.");
               System.out.println();
               System.out.println("4.  SECURITY RECOMMENDATION SUMMARY.");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print(" ENTER YOUR PROTECTING-EMAIL-CONFIDENTIALITY CHOICE (1 to 4): ");
            
            
               menuSelect = keyboard.nextInt();
            
               while (menuSelect < 1 || menuSelect > 4)
               
               {
               
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println("THIS IS INVALID CHOICE FOR PROTECTING-EMAIL-CONFIDENTIALITY SELECTION "); 
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW VALID PROTECTING-EMAIL-CONFIDENTIALITY SELECTIONS:");
                  System.out.println();
                  System.out.println("1. INTRODUCTION.");
                  System.out.println();
                  System.out.println("2. EMAIL TRANSMISSION SECURITY.");
                  System.out.println();
                  System.out.println("3. EMAIL CONTENT SECURITY.");
                  System.out.println();
                  System.out.println("4. SECURITY RECOMMENDATION SUMMARY.");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print(" ENTER YOUR PROTECTING-EMAIL-CONFIDENTIALITY CHOICE (1 to 4): ");
               
               
               
                  menuSelect = keyboard.nextInt();
               
               }
            
               System.out.println();
               System.out.println(" NOTE: There are eight performance attributes, or currencies, to be considered when evaluating whether a EMAIL-ISOLATION network can deliver on its full potential.".toUpperCase());
               System.out.println();                
               System.out.println(" NOTE:  Without all eight of these currencies, you don’t have a true EMAIL-ISOLATION network. With them, you have a powerful, game-changing platform for innovation .".toUpperCase());
               System.out.println(); 
            
               if ( menuSelect == 1)
               
               {          
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW INTRODUCTION: ");
                  System.out.println();
               
               
                  PEC.setINTR           (". ");
               
               
                  System.out.println               (" INTRODUCTION               = " +  PEC.getINTR());
                  System.out.println();          
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println( "TO CONTINUE WITH NEXT PROTECTING-EMAIL-CONFIDENTIALITY CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU  CHOICE # 1");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
               
               }
               
               else
               
                  if ( menuSelect == 2)
                  
                  {
                     System.out.println();
                     System.out.println();
                     System.out.println("PLEASE SEE BELOW EMAIL-TRANSMISSION-SECURITY: ");
                     System.out.println();
                  
                     PEC.setETS (". ");
                  
                  
                  
                     System.out.println(" MALWARE-INCIDENT DETECTION AND ANALYSIS             = " +  PEC.getETS());
                     System.out.println();
                     System.out.println("************************************************************************************************" );
                     System.out.println();
                     System.out.println( "TO CONTINUE WITH NEXT PROTECTING-EMAIL-CONFIDENTIALITY CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                     System.out.println();
                     System.out.println("************************************************************************************************" );   
                  
                  }
                  
                  else
                  
                     if ( menuSelect == 3 )
                     
                     {
                        System.out.println();
                        System.out.println();
                        System.out.println("PLEASE SEE BELOW EMAIL-CONTENT-SECURITY: ");
                        System.out.println();  
                     
                        PEC.setECS(". ");
                     
                        System.out.println(" EMAIL CONTENT SECURITY      = " +  PEC.getECS());    
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                        System.out.println();
                        System.out.println( "TO CONTINUE WITH NEXT PROTECTING-EMAIL-CONFIDENTIALITY CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                     
                     }
                     
                     else
                     
                        if ( menuSelect == 4)
                        
                        {
                           System.out.println();
                           System.out.println("PLEASE SEE BELOW SECURITY-RECOMMENDATION-SUMMARY: ");
                           System.out.println();
                        
                           PEC.setSRS(". ");
                        
                           System.out.println(" SECURITY RECOMMENDATION SUMMARY     = " + PEC.getSRS());      
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                           System.out.println();
                           System.out.println( "TO CONTINUE WITH NEXT PROTECTING-EMAIL-CONFIDENTIALITY CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                        
                        }
                        
                        
                        
                        else
                        
                           System.out.println();
               System.out.println   ("HERE ARE EMAIL-ISOLATION-FRAMEWORK MAIN MENU CATEGORIES LIST: ");
               System.out.println();
               System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
               System.out.println();
               System.out.println   ("2.  EMAIL STANDARDS ."); 
               System.out.println();
               System.out.println   ("3.  EMAIL SECURITY THREATS."); 
               System.out.println();
               System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
               System.out.println();
               System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
               System.out.println();
               System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
               System.out.println();
               System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
               System.out.println();
               System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
               System.out.println();
               System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
               System.out.println();
               System.out.println   ("12. SECURING EMAIL CLIENTS."); 
               System.out.println();
               System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
               System.out.println();
               System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
               System.out.println();
               System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
            
               menuSelection = keyboard.nextInt();
            
               while (menuSelection < 1 || menuSelection > 17) 
               
               {
               
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();  
                  System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("HERE IS THE VALID LIST OF EMAIL-ISOLATION MAIN MENU CATEGORIES: ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
                  System.out.println();
                  System.out.println   ("2.  EMAIL STANDARDS ."); 
                  System.out.println();
                  System.out.println   ("3.  EMAIL SECURITY THREATS."); 
                  System.out.println();
                  System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
                  System.out.println();
                  System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
                  System.out.println();
                  System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
                  System.out.println();
                  System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
                  System.out.println();
                  System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
                  System.out.println();
                  System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
                  System.out.println();
                  System.out.println   ("12. SECURING EMAIL CLIENTS."); 
                  System.out.println();
                  System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
                  System.out.println();
                  System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
                  System.out.println();
                  System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
               
               
               
                  menuSelection = keyboard.nextInt();
               
               } 
            
               break;
         
            case 16:
            
               EmailIsolationSetter RUBE;
               RUBE = new EmailIsolationSetter();
            
            
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println("YOU SELECTED REDUCING-UNSOLICTED-BULK-EMAIL CATEGORY FROM EMAIL-ISOLATION MAIN MENU ");
               System.out.println();
               System.out.println("PLEASE SEE BELOW REDUCING-UNSOLICTED-BULK-EMAIL CATEGORIES: ");
               System.out.println(); 
               System.out.println("1. INTRODUCTION.");
               System.out.println();
               System.out.println("2. WHY AN ORGANIZATION MAY WANT TO REDUCE UNSOLICITED BULK EMAIL.");
               System.out.println();
               System.out.println("3. TECHNIQUES TO REDUCE UNSOLICITED EMAIL.");
               System.out.println();
               System.out.println("4. USER EDUCATION.");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print(" ENTER YOUR REDUCING-UNSOLICTED-BULK-EMAIL CHOICE (1 to 4): ");
            
            
               menuSelect = keyboard.nextInt();
            
               while (menuSelect < 1 || menuSelect > 4)
               
               {
               
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println("THIS IS INVALID CHOICE FOR REDUCING-UNSOLICTED-BULK-EMAIL SELECTION "); 
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW VALID REDUCING-UNSOLICTED-BULK-EMAIL SELECTIONS:");
                  System.out.println();
                  System.out.println("1. INTRODUCTION.");
                  System.out.println();
                  System.out.println("2. WHY AN ORGANIZATION MAY WANT TO REDUCE UNSOLICITED BULK EMAIL.");
                  System.out.println();
                  System.out.println("3. TECHNIQUES TO REDUCE UNSOLICITED EMAIL.");
                  System.out.println();
                  System.out.println("4. USER EDUCATION.");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print(" ENTER YOUR REDUCING-UNSOLICTED-BULK-EMAIL CHOICE (1 to 4): ");
               
               
               
                  menuSelect = keyboard.nextInt();
               
               }
            
               System.out.println();
               System.out.println(" NOTE: There are eight performance attributes, or currencies, to be considered when evaluating whether a EMAIL-ISOLATION network can deliver on its full potential.".toUpperCase());
               System.out.println();                
               System.out.println(" NOTE:  Without all eight of these currencies, you don’t have a true EMAIL-ISOLATION network. With them, you have a powerful, game-changing platform for innovation .".toUpperCase());
               System.out.println(); 
            
               if ( menuSelect == 1)
               
               {          
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW INTRODUCTION: ");
                  System.out.println();
               
               
                  RUBE.setINTO (". ");
               
               
                  System.out.println               (" INTRODUCTION                = " +  RUBE.getINTO());
                  System.out.println();          
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println( "TO CONTINUE WITH NEXT REDUCING-UNSOLICTED-BULK-EMAIL CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU  CHOICE # 1");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
               
               }
               
               else
               
                  if ( menuSelect == 2)
                  
                  {
                     System.out.println();
                     System.out.println();
                     System.out.println("PLEASE SEE BELOW WHY-AN-ORGANIZATION-MAY-WANT-TO-REDUCE-UNSOLICITED-BULK-EMAIL: ");
                     System.out.println();
                  
                     RUBE.setWARB (". ");
                  
                  
                  
                     System.out.println(" WHY AN ORGANIZATION MAY WANT TO REDUCE UNSOLICITED BULK EMAIL             = " +  RUBE.getWARB());
                     System.out.println();
                     System.out.println("************************************************************************************************" );
                     System.out.println();
                     System.out.println( "TO CONTINUE WITH NEXT REDUCING-UNSOLICTED-BULK-EMAIL PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                     System.out.println();
                     System.out.println("************************************************************************************************" );   
                  
                  }
                  
                  else
                  
                     if ( menuSelect == 3 )
                     
                     {
                        System.out.println();
                        System.out.println();
                        System.out.println("PLEASE SEE BELOW TECHNIQUES-TO-REDUCE-UNSOLICITED-EMAIL: ");
                        System.out.println();  
                     
                        RUBE.setTRUE(". ");
                     
                        System.out.println(" TECHNIQUES TO REDUCE UNSOLICITED EMAIL     = " +  RUBE.getTRUE());    
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                        System.out.println();
                        System.out.println( "TO CONTINUE WITH NEXT REDUCING-UNSOLICTED-BULK-EMAIL CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                     
                     }
                     
                     else
                     
                        if ( menuSelect == 4)
                        
                        {
                           System.out.println();
                           System.out.println("PLEASE SEE BELOW  USER-EDUCATION: ");
                           System.out.println();
                        
                           RUBE.setUSRE(". ");
                        
                           System.out.println("  USER EDUCATION     = " + RUBE.getUSRE());      
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                           System.out.println();
                           System.out.println( "TO CONTINUE WITH NEXT REDUCING-UNSOLICTED-BULK-EMAIL CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                        
                        }
                        
                        
                        else
                        
                           System.out.println();
               System.out.println   ("HERE ARE EMAIL-ISOLATION-FRAMEWORK MAIN MENU CATEGORIES LIST: ");
               System.out.println();
               System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
               System.out.println();
               System.out.println   ("2.  EMAIL STANDARDS ."); 
               System.out.println();
               System.out.println   ("3.  EMAIL SECURITY THREATS."); 
               System.out.println();
               System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
               System.out.println();
               System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
               System.out.println();
               System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
               System.out.println();
               System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
               System.out.println();
               System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
               System.out.println();
               System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
               System.out.println();
               System.out.println   ("12. SECURING EMAIL CLIENTS."); 
               System.out.println();
               System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
               System.out.println();
               System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
               System.out.println();
               System.out.println   ("17. END USER EMAIL SECURITY."); 
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
            
               menuSelection = keyboard.nextInt();
            
               while (menuSelection < 1 || menuSelection > 17) 
               
               {
               
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();  
                  System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("HERE IS THE VALID LIST OF EMAIL-ISOLATION MAIN MENU CATEGORIES: ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
                  System.out.println();
                  System.out.println   ("2.  EMAIL STANDARDS ."); 
                  System.out.println();
                  System.out.println   ("3.  EMAIL SECURITY THREATS."); 
                  System.out.println();
                  System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
                  System.out.println();
                  System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
                  System.out.println();
                  System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
                  System.out.println();
                  System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
                  System.out.println();
                  System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
                  System.out.println();
                  System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
                  System.out.println();
                  System.out.println   ("12. SECURING EMAIL CLIENTS."); 
                  System.out.println();
                  System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
                  System.out.println();
                  System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
                  System.out.println();
                  System.out.println   ("17. END USER EMAIL SECURITY."); 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
               
               
               
                  menuSelection = keyboard.nextInt();
               
               } 
            
               break;
         
            case 17:
            
               EmailIsolationSetter EUSR;
               EUSR = new EmailIsolationSetter();
            
            
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println("YOU SELECTED END-USER-EMAIL-SECURITY CATEGORY FROM EMAIL-ISOLATION MAIN MENU ");
               System.out.println();
               System.out.println("PLEASE SEE BELOW END-USER-EMAIL-SECURITY CATEGORIES: ");
               System.out.println(); 
               System.out.println("1.  INTRODUCTION.");
               System.out.println();
               System.out.println("2.  WEBMAIL-CLIENTS.");
               System.out.println();
               System.out.println("3.  STANDALONE-CLIENTS.");
               System.out.println();
               System.out.println("4.  MAILBOX-SECURITY.");
               System.out.println();
               System.out.println("5.  SECURITY-RECOMMENDATIONS.");
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print(" ENTER YOUR END-USER-EMAIL-SECURITY CHOICE (1 to 5): ");
            
            
               menuSelect = keyboard.nextInt();
            
               while (menuSelect < 1 || menuSelect > 5)
               
               {
               
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println("THIS IS INVALID CHOICE FOR END-USER-EMAIL-SECURITY SELECTION "); 
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW VALID END-USER-EMAIL-SECURITY SELECTIONS:");
                  System.out.println();
                  System.out.println("1.  INTRODUCTION.");
                  System.out.println();
                  System.out.println("2.  WEBMAIL-CLIENTS.");
                  System.out.println();
                  System.out.println("3.  STANDALONE-CLIENTS.");
                  System.out.println();
                  System.out.println("4.  MAILBOX-SECURITY.");
                  System.out.println();
                  System.out.println("5.  SECURITY-RECOMMENDATIONS.");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print(" ENTER YOUR END-USER-EMAIL-SECURITY CHOICE (1 to 5): ");
               
               
               
                  menuSelect = keyboard.nextInt();
               
               }
            
               System.out.println();
               System.out.println(" NOTE: There are eight performance attributes, or currencies, to be considered when evaluating whether a EMAIL-ISOLATION network can deliver on its full potential.".toUpperCase());
               System.out.println();                
               System.out.println(" NOTE:  Without all eight of these currencies, you don’t have a true EMAIL-ISOLATION network. With them, you have a powerful, game-changing platform for innovation .".toUpperCase());
               System.out.println(); 
            
               if ( menuSelect == 1)
               
               {          
                  System.out.println();
                  System.out.println("PLEASE SEE BELOW INTRODUCTION: ");
                  System.out.println();
               
               
                  EUSR.setINTDN           (". ");
               
               
                  System.out.println               (" INTRODUCTION                = " +  EUSR.getINTDN());
                  System.out.println();          
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println( "TO CONTINUE WITH NEXT END-USER-EMAIL-SECURITY CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU  CHOICE # 1");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
               
               }
               
               else
               
                  if ( menuSelect == 2)
                  
                  {
                     System.out.println();
                     System.out.println();
                     System.out.println("PLEASE SEE BELOW WEBMAIL-CLIENTS: ");
                     System.out.println();
                  
                     EUSR.setWCLNT (". ");
                  
                  
                  
                     System.out.println(" WEBMAIL-CLIENTS             = " +  EUSR.getWCLNT());
                     System.out.println();
                     System.out.println("************************************************************************************************" );
                     System.out.println();
                     System.out.println( "TO CONTINUE WITH NEXT END-USER-EMAIL-SECURITY CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                     System.out.println();
                     System.out.println("************************************************************************************************" );   
                  
                  }
                  
                  else
                  
                     if ( menuSelect == 3 )
                     
                     {
                        System.out.println();
                        System.out.println();
                        System.out.println("PLEASE SEE BELOW STANDALONE-CLIENTS: ");
                        System.out.println();  
                     
                        EUSR.setSCLNT(". ");
                     
                        System.out.println(" STANDALONE CLIENTS      = " +  EUSR.getSCLNT());    
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                        System.out.println();
                        System.out.println( "TO CONTINUE WITH NEXT END-USER-EMAIL-SECURITY CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                        System.out.println();
                        System.out.println("************************************************************************************************" );
                     
                     }
                     
                     else
                     
                        if ( menuSelect == 4)
                        
                        {
                           System.out.println();
                           System.out.println("PLEASE SEE BELOW MAILBOX-SECURITY: ");
                           System.out.println();
                        
                           EUSR.setMBST(". ");
                        
                           System.out.println(" MAILBOX SECURITY     = " + EUSR.getMBST());      
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                           System.out.println();
                           System.out.println( "TO CONTINUE WITH NEXT END-USER-EMAIL-SECURITY CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                           System.out.println();
                           System.out.println("************************************************************************************************" );
                        
                        }
                        
                        else
                        
                           if ( menuSelect == 5)
                           
                           {
                              System.out.println();         
                              System.out.println();
                              System.out.println("PLEASE SEE BELOW SECURITY-RECOMMENDATIONS:"); 
                              System.out.println();     
                           
                           
                              EUSR.setSCRM(".");
                           
                           
                              System.out.println(" SECURITY RECOMMENDATIONS           = " + EUSR.getSCRM());
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                              System.out.println();
                              System.out.println( "TO CONTINUE WITH NEXT END-USER-EMAIL-SECURITY CATEGORY PLEASE SELECT AGAIN EMAIL-ISOLATION MAIN MENU CHOICE # 1");
                              System.out.println();
                              System.out.println("************************************************************************************************" );
                           
                           }
                           
                           
                           else
                           
                              System.out.println();
               System.out.println   ("HERE ARE EMAIL-ISOLATION-FRAMEWORK MAIN MENU CATEGORIES LIST: ");
               System.out.println();
               System.out.println   ("1. EMAIL ISOLATION ELEMENTS. "); 
               System.out.println();
               System.out.println   ("2.  EMAIL STANDARDS ."); 
               System.out.println();
               System.out.println   ("3.  EMAIL SECURITY THREATS."); 
               System.out.println();
               System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
               System.out.println();
               System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
               System.out.println();
               System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
               System.out.println();
               System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
               System.out.println();
               System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
               System.out.println();
               System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
               System.out.println();
               System.out.println   ("12. SECURING EMAIL CLIENTS."); 
               System.out.println();
               System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
               System.out.println();
               System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
               System.out.println();
               System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
               System.out.println();
               System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
               System.out.println();
               System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
               System.out.println();
               System.out.println("************************************************************************************************" );
               System.out.println();
               System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
            
               menuSelection = keyboard.nextInt();
            
               while (menuSelection < 1 || menuSelection > 17) 
               
               {
               
                  System.out.println(); 
                  System.out.println("************************************************************************************************" );
                  System.out.println();  
                  System.out.println("THIS IS INVALID CHOICE FOR EMAIL-ISOLATION MAIN MENU CATEGORY SELECTION");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println("HERE IS THE VALID LIST OF EMAIL-ISOLATION MAIN MENU CATEGORIES: ");
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.println   ("1.  EMAIL ISOLATION ELEMENTS. "); 
                  System.out.println();
                  System.out.println   ("2.  EMAIL STANDARDS ."); 
                  System.out.println();
                  System.out.println   ("3.  EMAIL SECURITY THREATS."); 
                  System.out.println();
                  System.out.println   ("4.  EMAIL ISOLATION USE-CASES."); 
                  System.out.println();
                  System.out.println   ("5.  EMAIL-MALWARE INCIDENTS PREVENTION."); 
                  System.out.println();
                  System.out.println   ("6.  EMAIL-MALWARE INCIDENTS RESPONSE."); 
                  System.out.println();
                  System.out.println   ("7.  SIGNING & ENCRYPTING EMAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("8.  PLANNING & MANAGING EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("9.  SECURING THE EMAIL SERVERS OPERATING SYSTEMS. "); 
                  System.out.println();
                  System.out.println   ("10. SECURING EMAIL SERVER CONTENTS ."); 
                  System.out.println();
                  System.out.println   ("11. IMPLEMENTING SECURE NETWORK INFRASTRUCTURE."); 
                  System.out.println();
                  System.out.println   ("12. SECURING EMAIL CLIENTS."); 
                  System.out.println();
                  System.out.println   ("13. ADMINISTERING THE EMAIL SERVERS."); 
                  System.out.println();
                  System.out.println   ("14. AUTHENTICATING A SENDING DOMAIN & E11MAIL MESSAGES."); 
                  System.out.println();
                  System.out.println   ("15. PROTECTING EMAIL CONFIDENTIALITY."); 
                  System.out.println();
                  System.out.println   ("16. REDUCING UNSOLICTED BULK EMAIL."); 
                  System.out.println();
                  System.out.println   ("17. END USER EMAIL SECURITY RECOMMENDATIONS."); 
                  System.out.println();
                  System.out.println("************************************************************************************************" );
                  System.out.println();
                  System.out.print("ENTER EMAIL-ISOLATION MAIN MENU CATEGORY CHOICE (1 - 17) FROM THE LIST ABOVE: ");
               
               
               
                  menuSelection = keyboard.nextInt();
               
               } 
               break; 
         
         }
   }
}

//*************************************END OF IOT TAXONOMY & FRAMEWORK PROGRAM***********************************************