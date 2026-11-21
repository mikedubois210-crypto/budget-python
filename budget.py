def calculer_budget():
    print("=== Calculateur de budget ===")
    revenu = float(input("Entrez votre revenu mensuel : "))
    loyer = float(input("Entrez le loyer ou charge fixe : "))
    courses = float(input("Entrez le budget courses/divers : "))

    total_depenses = loyer + courses
    solde = revenu - total_depenses

    print(f"\nTotal dépenses : {total_depenses:.2f}")
    print(f"Solde restant : {solde:.2f}")

    with open("resume_budget.txt", "w", encoding="utf-8") as f:
        f.write(f"Revenu : {revenu:.2f}\n")
        f.write(f"Total dépenses : {total_depenses:.2f}\n")
        f.write(f"Solde restant : {solde:.2f}\n")

    print("Résumé enregistré dans resume_budget.txt")

if __name__ == "__main__":
    calculer_budget()
