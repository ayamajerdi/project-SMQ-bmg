import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom'; 
import '../formation/FormationForm.css';
import { Navigate ,Link} from 'react-router-dom';
import Cookies from 'js-cookie';

function UpdateFormation() {
    const { id } = useParams();

    const [responsablesFormations, setResponsablesFormations] = useState([]);
    const [responsablesValidations, setResponsablesValidations] = useState([]);
    const [participantss, setParticipants] = useState([]);

    const [intitule_formation, setIntitule_formation] = useState('');
    const [type_formation, setType_formation] = useState('');
    const [organisme_formation, setOrganisme_formation] = useState('');
    const [theme_formation, setTheme_formation] = useState('');
    const [date_debut_formation, setDate_debut_formation] = useState('');
    const [date_fin_formation, setDate_fin_formation] = useState('');
    const [responsable_formationID, setResponsable_formation] = useState([]);
    const [responsable_validation, setResponsable_validation] = useState('');
    const [participantID, setParticipant] = useState([]);
    const [pieces_jointes, setPiecesJointes] = useState(null);
    const [piecesJointesUrl, setPiecesJointesUrl] = useState('');
    const [parametre_validation, setParametre_validation] = useState('');
    const [ajoutReussi, setAjoutReussi] = useState(false);

    

  useEffect(() => {

    const fetchEmploye = async () => {
        try {
          const response = await axios.get(`${process.env.REACT_APP_API_URL}/RH/formation/${id}/`);
          const data = response.data;
          setIntitule_formation(data.intitule_formation);
          setOrganisme_formation(data.organisme_formation);
          setTheme_formation(data.theme_formation);
          setType_formation(data.type_formation)
          setDate_debut_formation(data.date_debut_formation);
          setDate_fin_formation(data.date_fin_formation);
          setResponsable_formation(data.responsable_formation)
          setResponsable_validation(data.responsable_validation)
          setParticipant(data.participants);
          setParametre_validation(data.parametre_validation);
           if (data.pieces_jointes){
            setPiecesJointesUrl(`${data.pieces_jointes}`);
           }
        } catch (error) {
          console.error('Erreur lors de la récupération des données de formation:', error);
        }
      };
  
      fetchEmploye();


      axios.get(`${process.env.REACT_APP_API_URL}/RH/dashboard_employe/`)
      .then(response => {
        setResponsablesValidations(response.data);
      })
      .catch(error => {
          console.error('Erreur lors de la récupération des employés :', error);
      });
  axios.get(`${process.env.REACT_APP_API_URL}/RH/dashboard_formation/`)
      .then(response => {
        setResponsablesFormations(response.data);
      })
      .catch(error => {
          console.error('Erreur lors de la récupération des adresses :', error);
      });

  axios.get(`${process.env.REACT_APP_API_URL}/RH/dashboard_participant/`)
      .then(response => {
        setParticipants(response.data);
      })
      .catch(error => {
          console.error('Erreur lors de la récupération des départements :', error);
      });
}, [id]);

const handleFileChange = (event) => {
  const selectedFile = event.target.files[0];
  setPiecesJointes(selectedFile);
};


const handleSubmit = (event) => {
  event.preventDefault();
  
  const formData = new FormData();

        formData.append('intitule_formation', intitule_formation);
        formData.append('type_formation', type_formation);
        formData.append('organisme_formation', organisme_formation);
        formData.append('theme_formation', theme_formation);
        formData.append('date_debut_formation', date_debut_formation);
        formData.append('date_fin_formation', date_fin_formation);
        formData.append('responsable_validation', responsable_validation);
        participantID.forEach(id => {
            formData.append('participants', id);
        });
        responsable_formationID.forEach(id => {
            formData.append('responsable_formation', id);
        });
        formData.append('parametre_validation', parametre_validation);

        if (pieces_jointes) {
            formData.append('pieces_jointes', pieces_jointes);
        }
  const headers = {
    'Accept': '*/*',
    'Content-Type': 'multipart/form-data',
    'X-CSRFToken': Cookies.get('csrftoken')
};

    axios.put(`${process.env.REACT_APP_API_URL}/RH/update_fiche_employe/${id}/`, formData, { headers: headers })
      .then(response => {
        console.log('formation modifié avec succès :', response.data);
        setIntitule_formation('');
        setType_formation('');
        setOrganisme_formation('');
        setTheme_formation('');
        setDate_debut_formation('');
        setDate_fin_formation('');
        setResponsable_formation([]);
        setResponsable_validation('');
        setParticipant([]);
        setParametre_validation('');

        setAjoutReussi(true);
      })
      .catch(error => {
        console.error('Erreur lors de la modification du formation :', error);
      });
  };
  if(ajoutReussi){
    return <Navigate to={`/formation/${id}`} />;
  }

return (
    <div className="form-container">
    <div className="form-card">
        <h3>Ajouter une Formation</h3>
        <form onSubmit={handleSubmit} className="form">
            <div className="form-group">
                <label>Intitulé de la formation :</label>
                <input type="text" name="intitule_formation" value={intitule_formation} onChange={(e) => setIntitule_formation(e.target.value)} />
            </div>
            <div className="form-group">
                <label>Type de formation :</label>
                <select value={type_formation} onChange={(e) => setType_formation(e.target.value)}>
                <option value="">Sélectionner...</option>
                    <option value="interne">Formation en interne</option>
                    <option value="intra">Formation en intra</option>
                </select>
            </div>
            <div className="form-group">
                <label>Organisme de formation :</label>
                <input type="text" name="organisme_formation" value={organisme_formation} onChange={(e) => setOrganisme_formation(e.target.value)} />
            </div>
            <div className="form-group">
                <label>Thème de formation :</label>
                <input type="text" name="theme_formation" value={theme_formation} onChange={(e) => setTheme_formation(e.target.value)}></input>
            </div>
            <div className="form-group">
                <label>Date de début de la formation :</label>
                <input type="date" name="date_debut_formation" value={date_debut_formation} onChange={(e) => setDate_debut_formation(e.target.value)} />
            </div>
            <div className="form-group">
                <label>Date de fin de la formation :</label>
                <input type="date" name="date_fin_formation" value={date_fin_formation}onChange={(e) => setDate_fin_formation(e.target.value)} />
            </div>
            <div className="form-group">
                    <label>Responsables Formation :</label>
                    <select multiple value={responsable_formationID} onChange={(e) => setResponsable_formation(Array.from(e.target.selectedOptions, option => option.value))}>
                        {responsablesFormations.map(responsable_formation => (
                            <option key={responsable_formation.id} value={responsable_formation.id}>{responsable_formation.username}</option>
                        ))}
                    </select>
                </div>
            <div className="form-group">
                <label>Responsable de la validation :</label>
                <select value={responsable_validation} onChange={(e) => setResponsable_validation(e.target.value)}>
                <option value="">Sélectionner...</option>
                    {responsablesValidations.map(responsable_validation => (
                        <option key={responsable_validation.id} value={responsable_validation.id}>{responsable_validation.username}</option>
                    ))}
                </select>
            </div>
            <div className="form-group">
                    <label>Participants :</label>
                    <select multiple value={participantID} onChange={(e) => setParticipant(Array.from(e.target.selectedOptions, option => option.value))}>
                        {participantss.map(participants => (
                            <option key={participants.id} value={participants.id}>{participants.username}</option>
                        ))}
                    </select>
                </div>
                <div className="form-group">
                    <label>Paramètre de validation :</label>
                    <select value={parametre_validation} onChange={(e) => setParametre_validation(e.target.value)}>
                    <option value="">Sélectionner...</option>
                        <option value="chaud">Évaluation à chaud</option>
                        <option value="froid">Évaluation à froid</option>
                    </select>
                </div>
              <div className="form-group">
    <label>Pièces jointes :</label>
    {piecesJointesUrl ? (
        <div>
            <input 
                type="text" 
                value={piecesJointesUrl} 
                onChange={(e) => setPiecesJointesUrl(e.target.value)} 
            />
            <a href={piecesJointesUrl} target="_blank" rel="noopener noreferrer">Consulter</a>
        </div>
    ) : (
        <input 
            type="file" 
            onChange={handleFileChange} 
        />
    )}
</div>
              <button className="btn btn-success mt-3" type="submit">Modifier </button>
              <Link to="/Dashboardformation">
                  <button className="btn btn-gray mt-3">Retour au tableau de bord</button>
              </Link>
          </form>
      </div>
  </div>
);
}


export default UpdateFormation;
