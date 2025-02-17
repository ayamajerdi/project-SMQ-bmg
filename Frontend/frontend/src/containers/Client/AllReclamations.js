import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, Link } from 'react-router-dom';
import Cookies from 'js-cookie';
import './reclamations.css';

const Allreclamations = () => {
    const { id } = useParams();

    const [reclamations, setReclamations] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);
    const [deleting, setDeleting] = useState(false);

    useEffect(() => {
        const fetchReclamations = async () => {
            try {
                const response = await axios.get(`${process.env.REACT_APP_API_URL}/CRM/dashboard_reclamation_client/${id}/`, {
                    headers: {
                        'Accept': '*/*',
                    }
                });
                setReclamations(response.data);
            } catch (error) {
                console.error('Error fetching reclamations:', error);
                setError(error.message || 'Une erreur s\'est produite lors de la récupération des données.');
            } finally {
                setLoading(false);
            }
        };

        fetchReclamations();
    }, [id]);

    const handleDelete = async (reclamationId) => {
        const headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'X-CSRFToken': Cookies.get('csrftoken'),
        };
        try {
            setDeleting(true);
            await axios.delete(`${process.env.REACT_APP_API_URL}/CRM/delete_reclamation_client/${reclamationId}/`, { headers: headers });
            setReclamations(prevReclamations => prevReclamations.filter(client => client.id !== reclamationId));
        } catch (error) {
            console.error('Error deleting réclamation:', error);
            setError(error.message || 'Une erreur s\'est produite lors de la suppression du réclamation.');
        } finally {
            setDeleting(false);
        }
    };

    if (loading) {
        return <div>Chargement...</div>;
    }

    if (error) {
        return <div className="error-message">Erreur : {error}</div>;
    }

    return (
        <div className="reclamations-dashboard">
            <div className="reclamations-header">
                <h3>Liste des réclamations</h3>
            </div>
            <div className="reclamations-container">
                {reclamations.map(client => (
                    <div key={client.id} className={`reclamation-card ${client.declencher_plan_action ? 'show-additional-info' : ''}`}>
                        <div className="reclamation-card-body">
                            <p className="reclamation-card-text"><strong>Code Réclamation:</strong> {client.code}</p>
                            <p className="reclamation-card-text"><strong>Description:</strong> {client.description}</p>
                            <p className="reclamation-card-text"><strong>Type Réclamation:</strong> {client.type_reclamation}</p>
                            <p className="reclamation-card-text"><strong>Date Livraison:</strong> {client.date_livraison}</p>
                            <p className="reclamation-card-text"><strong>Gravité:</strong> {client.gravite}</p>
                            <p className="reclamation-card-text"><strong>Responsable Traitement:</strong> {client.responsable_traitement}</p>
                            <p className="reclamation-card-text"><strong>Décisions:</strong> {client.decisions}</p>
                            <p className="reclamation-card-text"><strong>Créé à:</strong> {client.created_at}</p>
                            <p className="reclamation-card-text"><strong>Créé par:</strong> {client.created_by}</p>
                            <p className="reclamation-card-text"><strong>Modifié à:</strong> {client.updated_at}</p>
                            <p className="reclamation-card-text"><strong>Modifié par:</strong> {client.updated_by}</p>
                            <p><strong>reclamation fournisseur :</strong> {client.reclamation_fournisseur ? <a href={`${process.env.REACT_APP_API_URL}/CRM/reclamations_fournisseur/${client.id}/`} target="_blank" rel="noopener noreferrer">Consulter</a> : 'null'}</p>
                            <p><strong>Plan action :</strong> {client.plan_action ? <a href={`${process.env.REACT_APP_API_URL}/CRM/plans_action/${client.id}/`} target="_blank" rel="noopener noreferrer">Consulter</a> : 'null'}</p>
                            <p><strong>Pièces jointes :</strong> {client.fichier_pdf ? <a href={`${process.env.REACT_APP_API_URL}/CRM/fichiers_pdf_reclamation_client/${client.id}/`} target="_blank" rel="noopener noreferrer">Consulter</a> : 'null'}</p>
                            {client.declencher_plan_action && (
                                <div className="additional-info">
                                    <p className="reclamation-card-text"><strong>Date Détection:</strong> {client.date_detection}</p>
                                    <p className="reclamation-card-text"><strong>Désignation Produit Non Conforme:</strong> {client.designation_produit_non_conforme}</p>
                                    <p className="reclamation-card-text"><strong>Description Non Conformité:</strong> {client.description_non_conformite}</p>
                                    <p className="reclamation-card-text"><strong>Produits Non Conformes:</strong> {client.produits_non_conformes}</p>
                                    <p className="reclamation-card-text"><strong>Type Non Conformité:</strong> {client.type_non_conformite}</p>
                                    <p className="reclamation-card-text"><strong>Source Non Conformité:</strong> {client.source_non_conformite}</p>
                                    <p className="reclamation-card-text"><strong>Niveau Gravité:</strong> {client.niveau_gravite}</p>
                                    <p className="reclamation-card-text"><strong>Pièces jointes :</strong> {client.pieces_jointes ? <a href={`${process.env.REACT_APP_API_URL}/produit/pieces_jointes_produit/${client.id}/`} target="_blank" rel="noopener noreferrer">Consulter</a> : 'null'}</p>
                                    <p className="reclamation-card-text"><strong>Personnes à Notifier:</strong> {client.personnes_a_notifier}</p>
                                </div>
                            )}
                        </div>
                        <div className="reclamation-card-buttons">
                            <Link to={`/ModifierReclamation/${client.id}`} className="btn btn-primary">Modifier</Link>
                            <button onClick={() => handleDelete(client.id)} className="btn btn-danger" disabled={deleting}>Supprimer</button>
                        </div>
                    </div>
                ))}
            </div>
            <div className="dashboard-actions">
                <Link to={`/CréerReclamationClient/${id}/`} className="btn btn-primary">Ajouter Réclamation</Link>
            </div>
            <div className="dashboard-actions">
                <Link to={`/ConsulterClient/${id}`} className="btn btn-secondary">Retour</Link>
            </div>
        </div>
    );
};

export default Allreclamations;
