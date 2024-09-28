# bank_summary

Permets de grouper les transactions à partir de l'historique de transaction d'un compte banque populaire ou crédit mutuel. 

## Banque populaire

Nécessite de télécharger la page d'historique.

Parser la page avec banquepopulaire_load_transactions et grouper pour avoir une vue d'ensemble avec aggregate_transactions.py .

## Crédit mutuel

Nécessite de télécharger .csv d'exports.

Parser la page avec creditmutuel_load_transactions et grouper pour avoir une vue d'ensemble avec aggregate_transactions.py . 