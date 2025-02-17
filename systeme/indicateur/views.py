from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import *
from .models import*
from django.contrib.auth.decorators import login_required
from django.http import FileResponse


def get_piece_jointe_indicateur(request, fiche_id):
    fiche = get_object_or_404(Indicateur, id=fiche_id)
    piece_jointe_path = fiche.piece_jointe.path
    return FileResponse(open(piece_jointe_path, 'rb'), content_type='application/pdf')

def get_piece_jointe_suivi(request, fiche_id):
    fiche = get_object_or_404(SuiviIndicateur, id=fiche_id)
    piece_jointe_path = fiche.piece_jointe.path
    return FileResponse(open(piece_jointe_path, 'rb'), content_type='application/pdf')


# Afficher tous les Indicateur

@method_decorator(login_required(login_url='login'), name='dispatch')
class DashboardIndicateurAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        indicateurs = Indicateur.objects.all()
        data = []
        for indicateur in indicateurs:
            indicateur_data = {
                'id': indicateur.id,
                'Libelle': indicateur.libelle,
                'type_indicateur': indicateur.type_indicateur,
                'processus_lie': indicateur.processus_lie,
                'axe_politique_qualite': indicateur.axe_politique_qualite,
                'type_resultat_attendu': indicateur.type_resultat_attendu,
                'piece_jointe': indicateur.piece_jointe.url if indicateur.piece_jointe else None,
            }
            data.append(indicateur_data)
        return Response(data, status=status.HTTP_200_OK)

# Ajouter un Indicateur
@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateIndicateurAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = IndicateurSerializer(data=request.data)
        if serializer.is_valid():
            created_at = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            serializer.validated_data['created_at'] = created_at
            serializer.save(created_by=request.user)
            indicateur_data = serializer.data
            indicateur_data['created_by'] = request.user.first_name
            indicateur_data['created_at'] = created_at
            indicateur_data['id'] = serializer.instance.id 
            return Response(indicateur_data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Modifier un Indicateur
@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateIndicateurAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, pk):
        indicateur = get_object_or_404(Indicateur, pk=pk)
        serializer = IndicateurSerializer(indicateur, data=request.data)
        if serializer.is_valid():
            updated_at = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            serializer.validated_data['updated_at'] = updated_at
            serializer.save(updated_by=request.user)
            indicateur.save()
            indicateur_data = serializer.data
            indicateur_data['updated_by'] = request.user.first_name
            indicateur_data['updated_at'] = updated_at
            return Response(indicateur_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Afficher un Indicateur
@method_decorator(login_required(login_url='login'), name='dispatch')
class SingularIndicateurAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        indicateur = get_object_or_404(Indicateur, pk=pk)
        created_by_name = indicateur.created_by.first_name if indicateur.created_by else None
        updated_by_name = indicateur.updated_by.first_name if indicateur.updated_by else None
        created_at_str = indicateur.created_at.strftime('%Y-%m-%d %H:%M:%S') if indicateur.created_at else None
        updated_at_str = indicateur.updated_at.strftime('%Y-%m-%d %H:%M:%S') if indicateur.updated_at else None
        indicateur_data={
                'id': indicateur.id,
                'Libelle': indicateur.libelle,
                'type_indicateur': indicateur.type_indicateur,
                'processus_lie': indicateur.processus_lie,
                'axe_politique_qualite': indicateur.axe_politique_qualite,
                'type_resultat_attendu': indicateur.type_resultat_attendu,
                'date_debut': indicateur.date_debut,
                'periodicite_indicateur': indicateur.periodicite_indicateur,
                'type_suivi': indicateur.type_suivi,
                'valeur_cible': indicateur.valeur_cible,
                'limite_critique': indicateur.limite_critique,
                'piece_jointe': indicateur.piece_jointe.url if indicateur.piece_jointe else None,
                'created_by': created_by_name,
                'updated_by': updated_by_name,
                'created_at': created_at_str,
                'updated_at': updated_at_str,
            }
        serializer = IndicateurSerializer(indicateur)
        serialized_data = serializer.data
        serialized_data['created_by'] = indicateur.created_by.first_name 
        serialized_data['updated_by'] = indicateur.updated_by.first_name if indicateur.updated_by else None
        serialized_data['created_at'] = indicateur.created_at.strftime('%Y-%m-%d %H:%M:%S') 
        serialized_data['updated_at'] = indicateur.updated_at.strftime('%Y-%m-%d %H:%M:%S') if indicateur.updated_at else None
        return Response(indicateur_data)

# Supprimer un Indicateur
@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteIndicateurAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        indicateur = get_object_or_404(Indicateur, pk=pk)
        indicateur.delete()
        return Response({"message": "L indicateur a été supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)
    


# Afficher tous les SuiviIndicateur

@method_decorator(login_required(login_url='login'), name='dispatch')
class DashboardSuiviIndicateurAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,pk):
        indi = get_object_or_404(Indicateur, pk=pk)
        SuiviIndicateurs = SuiviIndicateur.objects.filter(indicateur=indi)
        data = []
        for suiviIndicateur in SuiviIndicateurs:
            created_by_name = suiviIndicateur.created_by.first_name if suiviIndicateur.created_by else None
            updated_by_name = suiviIndicateur.updated_by.first_name if suiviIndicateur.updated_by else None
            created_at_str = suiviIndicateur.created_at.strftime('%Y-%m-%d %H:%M:%S') if suiviIndicateur.created_at else None
            updated_at_str = suiviIndicateur.updated_at.strftime('%Y-%m-%d %H:%M:%S') if suiviIndicateur.updated_at else None
            suiviIndicateur_data = {
                'id': suiviIndicateur.id,
                'frequence': suiviIndicateur.frequence,
                'objectif': suiviIndicateur.objectif,
                'limite_critique': suiviIndicateur.limite_critique,
                'resultat': suiviIndicateur.resultat,
                'commentaire': suiviIndicateur.commentaire,
                'piece_jointe': suiviIndicateur.piece_jointe.url if suiviIndicateur.piece_jointe else 'pas de fichier',
                'created_by': created_by_name,
                'created_at': created_at_str,


            }
            data.append(suiviIndicateur_data)
        return Response(data, status=status.HTTP_200_OK)

# Ajouter un SuiviIndicateur
@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateSuiviIndicateurAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        indi = get_object_or_404(Indicateur, pk=pk)
        
        if indi.type_suivi != 'manuel':
            return Response(
                {"detail": "Cette operation concerne les indicateurs de tpe suivi : manuel ."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = SuiviIndicateurSerializer(data=request.data)
        if serializer.is_valid():
            created_at = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            serializer.validated_data['created_at'] = created_at
            serializer.save(created_by=request.user, indicateur=indi)
            suivi_data = serializer.data
            suivi_data['created_by'] = request.user.first_name
            suivi_data['created_at'] = created_at
            return Response(suivi_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Modifier un SuiviIndicateur
@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateSuiviIndicateurAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, pk):
        suiviIndicateur = get_object_or_404(SuiviIndicateur, pk=pk)
        serializer = SuiviIndicateurSerializer(suiviIndicateur, data=request.data)
        if serializer.is_valid():
            updated_at = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            serializer.validated_data['updated_at'] = updated_at
            serializer.save(updated_by=request.user)
            suiviIndicateur.save()
            suiviIndicateur_data = serializer.data
            suiviIndicateur_data['updated_by'] = request.user.first_name
            suiviIndicateur_data['updated_at'] = updated_at
            return Response(suiviIndicateur_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Afficher un SuiviIndicateur
@method_decorator(login_required(login_url='login'), name='dispatch')
class SingularSuiviIndicateurAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        suiviIndicateur = get_object_or_404(SuiviIndicateur, pk=pk)
        serializer = SuiviIndicateurSerializer(suiviIndicateur)
        serialized_data = serializer.data
        serialized_data['created_by'] = suiviIndicateur.created_by.first_name 
        serialized_data['updated_by'] = suiviIndicateur.updated_by.first_name 
        serialized_data['created_at'] = suiviIndicateur.created_at.strftime('%Y-%m-%d %H:%M:%S') if suiviIndicateur.created_at else None
        serialized_data['updated_at'] = suiviIndicateur.updated_at.strftime('%Y-%m-%d %H:%M:%S') if suiviIndicateur.updated_at else None
        return Response(serialized_data)

# Supprimer un SuiviIndicateur
@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteSuiviIndicateurAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        suiviIndicateur = get_object_or_404(SuiviIndicateur, pk=pk)
        suiviIndicateur.delete()
        return Response({"message": "L SuiviIndicateur a été supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)
    