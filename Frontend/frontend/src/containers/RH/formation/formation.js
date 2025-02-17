import React, { useState, useEffect } from 'react';
import { useParams, Link, Navigate } from 'react-router-dom'; 
import axios from 'axios';
import Cookies from 'js-cookie';
import './details.css'


const FormationDetail = () => {
  const { id } = useParams();
  const [formation, setFormation] = useState(null);
  const [responsableValidationName, setResponsableValidationName] = useState('');
  const [responsableFormationName, setResponsableFormationName] = useState([]);
  const [participantsNames, setParticipantsNames] = useState([]);

  const [deleteReussi, setDeleteReussi] = useState(false);

  useEffect(() => {
    const fetchFormation = async () => {
      try {
        const response = await axios.get(`${process.env.REACT_APP_API_URL}/RH/formation/${id}/`);
        setFormation(response.data);

        const responsableValidationResponse = await axios.get(`${process.env.REACT_APP_API_URL}/RH/employe/${response.data.responsable_validation}/`);
        setResponsableValidationName(responsableValidationResponse.data.username);


        const responsableDetails = await Promise.all(response.data.responsable_formation.map(async (responsableID) => {
          const responsablereponse = await axios.get(`${process.env.REACT_APP_API_URL}/RH/responsable_formation/${responsableID}/`);
          return responsablereponse.data.username;
      }));
      setResponsableFormationName(responsableDetails);

        const participantsDetails = await Promise.all(response.data.participants.map(async (participantId) => {
          const participantResponse = await axios.get(`${process.env.REACT_APP_API_URL}/RH/participant/${participantId}/`);
          return participantResponse.data.username;
      }));
      setParticipantsNames(participantsDetails);

      } catch (error) {
        console.error('Erreur lors de la récupération des données de formation:', error);
      }
    };

    fetchFormation();
  }, [id]);

  const handleDelete = async () => {
    const headers = {
      'Accept': '*/*',
      'Content-Type': 'application/json',
      'X-CSRFToken': Cookies.get('csrftoken'),
    };
    try {
      await axios.delete(`${process.env.REACT_APP_API_URL}/RH/delete_formation/${id}/`, { headers: headers });
      setDeleteReussi(true);
    } catch (error) {
      console.error('Erreur lors de la suppression de la fiche:', error);
    }
  };

  if (deleteReussi) {
    return <Navigate to="/Dashboardformation" />;
  }
    return (
      <div>
      {formation ? (
          <div className="card">
              <div className="card-body">
                  <h3>Détails de la Formation</h3>
                  <div className="detail">
                      <strong>ID :</strong> {formation.id}
                  </div>
                  <div className="detail">
                      <strong>Intitulé de la formation :</strong> {formation.intitule_formation}
                  </div>
                  <div className="detail">
                      <strong>Type de formation :</strong> {formation.type_formation}
                  </div>
                  <div className="detail">
                      <strong>Organisme de formation :</strong> {formation.organisme_formation}
                  </div>
                  <div className="detail">
                      <strong>Thème de formation :</strong> {formation.theme_formation}
                  </div>
                  <div className="detail">
                      <strong>Date de début de la formation :</strong> {formation.date_debut_formation}
                  </div>
                  <div className="detail">
                      <strong>Date de fin de la formation :</strong> {formation.date_fin_formation}
                  </div>
                  <div className="detail">
                      <strong>Responsable de la validation :</strong> {responsableValidationName}
                  </div>
                  <div className="detail">
                      <strong>Responsable de la Formation :</strong> {responsableFormationName.join(', ')}
                  </div>
                  <div className="detail">
                      <strong>Date de création :</strong> {formation.created_at}
                  </div>
                  <div className="detail">
                      <strong>Créé par :</strong> {formation.created_by}
                  </div>
                  <div className="detail">
                      <strong>Modifié par :</strong> {formation.updated_by}
                  </div>
                  <div className="detail">
                      <strong>Date de modification :</strong> {formation.updated_at}
                  </div>
                  <div className="detail">
                      <strong>Participants :</strong>{participantsNames.join(', ')}
                  </div>
                  <div className="detail">
                      <strong>Paramètre de validation :</strong> {formation.parametre_validation}
                  </div>
                  <div className="detail">
                      <strong>Date de clôture de la formation :</strong> {formation.date_cloture}
                  </div>
                  <div className="detail">
                      <strong>Pièces jointes :</strong> {formation.pieces_jointes ? <a href={`${process.env.REACT_APP_API_URL}/RH/piece_jointe_formation/${id}/`} target="_blank" rel="noopener noreferrer">Consulter</a> : 'null'}
                  </div>
              </div>
              <div className="button-group">
                  <a href="/Dashboardformation" className="btn btn-secondary">Retour</a>
                  <Link to={`/update-formation/${formation.id}`} className="btn btn-primary">Modifier</Link>
                  <button className="btn btn-danger" onClick={handleDelete}>Supprimer</button>
              </div>
          </div>
      ) : (
          <p>Chargement...</p>
      )}
  </div>
  
    );
};

export default FormationDetail;
