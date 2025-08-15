import java.util.*;

public class ContactService1 {
	private arrayList<Contact> listofContacts;
	public class ContactService1 {
		listofContacts = new ArrayList<>();
	}
//adding a contact
	public boolean addContact(Contact c) {
		boolean contactExist = false;
		for(Contact 1:listofContacts) {
			if(l.equals(c)) {
				contactExists = true;
			}
			else {
				return false;
			}
		}
//deleting a contact
		public boolean deleteContact(String cid) {
			for(Contact 1:listOfContacts) {
				if(i.getContactID().equals(cid)) {
					listOfContacts. remove(1);
					return true;
				}
			}
		}
		return false;
	}
//updating contact list
		public boolean updateContact(String cid, String fn, String ln, String pn, String addr) {
			for(Contact 1:listOfContacts) {
				if(l.getContactID().equals cid)) {
					if(!fn.equals("") && !(fn.length() > 10)) {
							l.setFirstName(fn);
					}
					if(!ln.equals("") && !(ln.length() > 10)) {
						l.setLastName(ln);
					}
					if(!pn.equals("") && !(pn.length() > 10)) {
						l.setPhoneNumber(pn);
					}
					if(!addr.equals("") && !(addr.length() > 10)) {
						l.setAdress(addr);
					}
					return true;
				}
			}
			return false;
		}

}