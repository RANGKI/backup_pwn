import scapy.all as scapy

# Reverse character mapping (keys and values swapped)
characters_reverse = {v: k for k, v in {
    "A":"key  8[ras]116", "B":"key  8[ras]119", "C":"key  8[ras]118", "D":"key  8[ras]113", "E":"key  8[ras]112", 
    "F":"key  8[ras]115", "G":"key  8[ras]114", "H":"key  8[ras]125", "I":"key  8[ras]124", "J":"key  8[ras]127", 
    "K":"key  8[ras]126", "L":"key  8[ras]121", "M":"key  8[ras]120", "N":"key  8[ras]123", "O":"key  8[ras]122", 
    "P":"key  8[ras]101", "Q":"key  8[ras]100", "R":"key  8[ras]103", "S":"key  8[ras]102", "T":"key  7[ras]97", 
    "U":"key  7[ras]96", "V":"key  7[ras]99", "W":"key  7[ras]98", "X":"key  8[ras]109", "Y":"key  8[ras]108", 
    "Z":"key  8[ras]111",

    "a":"key  7[ras]84", "b":"key  7[ras]87", "c":"key  7[ras]86", "d":"key  7[ras]81", "e":"key  7[ras]80", 
    "f":"key  7[ras]83", "g":"key  7[ras]82", "h":"key  7[ras]93", "i":"key  7[ras]92", "j":"key  7[ras]95", 
    "k":"key  7[ras]94", "l":"key  7[ras]89", "m":"key  7[ras]88", "n":"key  7[ras]91", "o":"key  7[ras]90", 
    "p":"key  7[ras]69", "q":"key  7[ras]68", "r":"key  7[ras]71", "s":"key  7[ras]70", "t":"key  7[ras]65", 
    "u":"key  7[ras]64", "v":"key  7[ras]67", "w":"key  7[ras]66", "x":"key  7[ras]77", "y":"key  7[ras]76", 
    "z":"key  7[ras]79",

    "1":"key  6[ras]4", "2":"key  6[ras]7", "3":"key  6[ras]6", "4":"key  6[ras]1", "5":"key  6[ras]0",
    "6":"key  6[ras]3", "7":"key  6[ras]2", "8":"key  7[ras]13", "9":"key  7[ras]12", "0":"key  6[ras]5",

    "\n":"key  3RTN", "\b":"key  3BAS", " ":"key  7[ras]21",

    "+":"key  7[ras]30", "=":"key  6[ras]8", "/":"key  7[ras]26", "_":"key  8[ras]106", "<":"key  6[ras]9", 
    ">":"key  7[ras]11", "[":"key  8[ras]110", "]":"key  8[ras]104", "!":"key  7[ras]20", "@":"key  8[ras]117", 
    "#":"key  7[ras]22", "$":"key  7[ras]17", "%":"key  7[ras]16", "^":"key  8[ras]107", "&":"key  7[ras]19", 
    "*":"key  7[ras]31", "(":"key  7[ras]29", ")":"key  7[ras]28", "-":"key  7[ras]24", "'":"key  7[ras]18", 
    '"':"key  7[ras]23", ":":"key  7[ras]15", ";":"key  7[ras]14", "?":"key  7[ras]10", "`":"key  7[ras]85", 
    "~":"key  7[ras]75", "\\":"key  8[ras]105", "|":"key  7[ras]73", "{":"key  7[ras]78", "}":"key  7[ras]72",
    ",":"key  7[ras]25", ".":"key  7[ras]27"
}.items()}

def extract_secret_message(pcap_file):
    """
    Extract hidden secret message from ICMP packets in a PCAP file
    """
    secret_message = []
    
    # Read the PCAP file
    packets = scapy.rdpcap(pcap_file)
    
    # Process packets in pairs
    for i in range(0, len(packets), 2):
        # Ensure we have a pair of packets
        if i + 1 < len(packets):
            request_packet = packets[i]
            reply_packet = packets[i + 1]
            
            # Check if packets are ICMP with payloads and have same packet ID
            if (request_packet.haslayer(scapy.ICMP) and request_packet.haslayer(scapy.Raw) and
                reply_packet.haslayer(scapy.ICMP) and reply_packet.haslayer(scapy.Raw) and
                request_packet[scapy.ICMP].id == reply_packet[scapy.ICMP].id):
                
                # Decode the payload from the request packet
                payload = request_packet[scapy.Raw].load.decode('utf-8', errors='ignore')
                
                # Check if payload is a known key command
                if payload in characters_reverse:
                    secret_message.append(characters_reverse[payload])
    
    return ''.join(secret_message)

def main():
    # Prompt for PCAP file path
    pcap_file = input("Enter the path to the PCAP file: ")
    
    try:
        # Extract and print the secret message
        message = extract_secret_message(pcap_file)
        print(f"Extracted Secret Message: {message}")
    except Exception as e:
        print(f"Error extracting message: {e}")

if __name__ == "__main__":
    main()