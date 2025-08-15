import java.util.*;

public class ContactService1 {
	private HashMap<Contact> listofContacts;
	public class ContactService1 {
		listofContacts = new HashMap<>()<>();
	}
}

// Software Design and Development Enhancement begins at line 16


// Algorithms and Data Structures Enhancement begins at line 51


// Software Design and Development Enhancement Begins Here

// Adding a contact function to validate information
FUNCTION addContact(Contact contact):
 IF validateContact(contact):
  IF contactAlreadyExists(contact):
   THROW ContactExistsException
ELSE:
	contactsMap.put(contact.contactID, contact)
ELSE:
	   THROW InvalidInputException
 END FUNCTION
		
// Validating contact input information
FUNCTION validateContact(Contact contact):
	IF contact.firstName.length > 10 OR contact.lastName.length > 10:
		RETURN false
		   IF NOT contact.phoneNumber.matches("^[0-9]{10}$"):
		    RETURN false
			 RETURN true
END FUNCTION

// Streamlining the update contact process more efficient
FUNCTION updateContact(String contactID, String newFirstName, String newLastName, String newPhoneNumber, String newAddress):
Contact contact = contactsMap.get(contactID)
	IF contact EXISTS:
		IF newFirstName NOT empty:
			contact.setFirstName(newFirstName)
				IF newLastName NOT empty:
					contact.setLastName(newLastName)
					   IF newPhoneNumber.matches("^[0-9]{10}$"):
                        contact.setPhoneNumber(newPhoneNumber)
End FUNCTION


// Algorithm and Data Structures Enhancement Begins Here

// Replace the ArrayList with HashMap 
HashMap<String, Contact> contactsMap = new HashMap<>();

// Add a contact to the HashMap 
FUNCTION addContact(Contact contact):
 IF contactsMap.containsKey(contact.contactID):
  THROW ContactExistsException
 ELSE: 
   contactsMap.put(contact.contactID, contact)
END FUNCTION

 // Update the contact information
 FUNCTION updateContact(String contactID, String newFirstName, String newLastName, String newPhoneNumber, String newAddress):
  Contact contact = contactsMap.get(contactID)
   IF contact EXISTS:
    IF newFirstName NOT empty:
	 contact.setFirstName(newFirstName)
	  IF newLastName NOT empty:
	   contact.setLastName(newLastName)
	    IF newPhoneNumber.matches("^[0-9]{10}$"):
		 contact.setPhoneNumber(newPhoneNumber)
		  IF newAddress NOT empty:
		   contact.setAddress(newAddress)
		    ELSE:
			 THROW ContactNotFoundException
END FUNCTION 

// Deleting any contact information
FUNCTION deleteContact(String contactID):
 IF contactsMap.containsKey(contactID):
  contactsMap.remove(contactID)
 ELSE:
  THROW ContactNotFoundException
END FUNCTION

 // Retrieving contact information faster
FUNCTION getContact(String contactID):
 RETURN contactsMap.get(contactID)
END FUNCTION

