import { useEffect, useState } from "react";
import "./App.css";
import ContactLists from "./components/ContactLists";
import ContactForm from "./components/ContactForm";

function App() {
  const [contacts, setContacts] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentContact, setCurrentContact] = useState({});

  const fetchContacts = async () => {
    const response = await fetch("http://127.0.0.1:5000/contacts");
    const data = await response.json();
    setContacts(data.contacts);
    console.log(data.contacts);
  };

  useEffect(() => {
    fetchContacts();
  }, []);

  const closeModal = () => {
    setIsModalOpen(false);
    setCurrentContact({});
  };

  const openCreateModal = () => {
    if (!isModalOpen) {
      setIsModalOpen(true);
    }
  };

  const openEditModal = (contact) => {
    if (isModalOpen) return;

    setCurrentContact(contact);
    setIsModalOpen(true);
  };

  const onUpdate = () => {
    closeModal();
    fetchContacts();
  };

  return (
    <div>
      <ContactLists
        contacts={contacts}
        updateContact={openEditModal}
        updateCallback={onUpdate}
      />
      <button onClick={openCreateModal}>Create New Contact</button>
      {isModalOpen && (
        <div>
          <div>
            <span onClick={closeModal}>&times;</span>
            <ContactForm
              existingContact={currentContact}
              updateCallback={onUpdate}
            />
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
