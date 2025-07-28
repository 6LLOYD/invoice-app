import React, { useState } from 'react';
import {
  DndContext,
  closestCenter,
  KeyboardSensor,
  PointerSensor,
  useSensor,
  useSensors,
} from '@dnd-kit/core';
import {
  arrayMove,
  SortableContext,
  sortableKeyboardCoordinates,
  useSortable,
} from '@dnd-kit/sortable';
import { CSS } from '@dnd-kit/utilities';
import '../css/Devis.css';

interface Item {
  id: string;
  description: string;
  prix_unitaire: number;
}

interface SortableItemProps {
  id: string;
  description: string;
  prix_unitaire: number;
}

const SortableItem: React.FC<SortableItemProps> = ({ id, description, prix_unitaire }) => {
  const {
    attributes,
    listeners,
    setNodeRef,
    transform,
    transition,
  } = useSortable({ id });

  const style = {
    transform: CSS.Transform.toString(transform),
    transition,
    padding: '1rem',
    backgroundColor: 'var(--primary-color-1)',
    border: '1px solid var(--primary-color-2)',
    borderRadius: '8px',
    cursor: 'grab',
    marginBottom: '0.5rem',
  };

  return (
    <div ref={setNodeRef} style={style} {...attributes} {...listeners}>
      {description} - {prix_unitaire}€
    </div>
  );
};

const Devis: React.FC = () => {
  const [selectedClient, setSelectedClient] = useState<string | null>(null);
  const [items, setItems] = useState<Item[]>([]);
  const [availableItems, setAvailableItems] = useState<Item[]>([
    { id: 'i1', description: 'Peinture murale', prix_unitaire: 50 },
    { id: 'i2', description: 'Pose parquet', prix_unitaire: 80 },
  ]);
  const [date, setDate] = useState<string>('');

  const clients = [
    { id: '1', nom: 'Jean Dupont' },
    { id: '2', nom: 'Marie Curie' },
  ];

  const sensors = useSensors(
    useSensor(PointerSensor),
    useSensor(KeyboardSensor, {
      coordinateGetter: sortableKeyboardCoordinates,
    })
  );

  const handleDragEnd = (event: any) => {
    const { active, over } = event;
    if (active.id !== over.id) {
      const activeIndex = availableItems.findIndex(item => item.id === active.id);
      const overIndex = items.findIndex(item => item.id === over.id) !== -1
        ? items.findIndex(item => item.id === over.id) + availableItems.length
        : availableItems.findIndex(item => item.id === over.id);

      if (activeIndex !== -1 && overIndex >= availableItems.length) {
        const movedItem = availableItems[activeIndex];
        setAvailableItems(availableItems.filter(item => item.id !== active.id));
        setItems([...items, movedItem]);
      } else if (activeIndex >= availableItems.length && overIndex < availableItems.length) {
        const movedItem = items[activeIndex - availableItems.length];
        setItems(items.filter(item => item.id !== active.id));
        setAvailableItems([...availableItems, movedItem]);
      }
    }
  };

  const handleSubmit = () => {
    const data = {
      numero: `D-${Date.now()}`, // Génération temporaire
      date,
      total_ht: items.reduce((sum, item) => sum + item.prix_unitaire, 0),
      tva_taux: 5.5,
      type_document: 'Devis',
      client_id: selectedClient,
      items: items.map(item => ({ description: item.description, prix_unitaire: item.prix_unitaire })),
    };
    console.log('Envoi au backend:', data);
    // Remplace console.log par un appel API avec createDocument si implémenté
  };

  return (
    <div className="devis-container">
      <h2>Sélectionner un client</h2>
      <div className="client-cards">
        {clients.map(client => (
          <div
            key={client.id}
            className={`client-card ${selectedClient === client.id ? 'selected' : ''}`}
            onClick={() => setSelectedClient(client.id)}
          >
            {client.nom}
          </div>
        ))}
      </div>

      <h2>Date</h2>
      <input
        type="date"
        value={date}
        onChange={(e) => setDate(e.target.value)}
        className="date-input"
      />

      <h2>Ajouter des items</h2>
      <DndContext sensors={sensors} collisionDetection={closestCenter} onDragEnd={handleDragEnd}>
        <div className="drag-drop-area">
          <h3>Items disponibles</h3>
          <SortableContext items={availableItems}>
            {availableItems.map((item) => (
              <SortableItem key={item.id} id={item.id} description={item.description} prix_unitaire={item.prix_unitaire} />
            ))}
          </SortableContext>

          <h3>Items sélectionnés</h3>
          <SortableContext items={items}>
            {items.map((item) => (
              <SortableItem key={item.id} id={item.id} description={item.description} prix_unitaire={item.prix_unitaire} />
            ))}
          </SortableContext>
        </div>
      </DndContext>

      <button className="btn btn-primary mt-3" onClick={handleSubmit}>
        Générer Devis
      </button>
    </div>
  );
};

export default Devis;