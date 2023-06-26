import csv
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import rdMolDraw2D

csv_file = 'yourCSVFileName.csv' #Replace

# Read the CSV file and store the data in a list
with open(csv_file, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)  # Skip the header row if there's one
    csv_data = [row for row in reader]

# Iterate through the rows of the CSV data
for row in csv_data:
    smiles = row[0]
    mol_name = row[1]
    CAS = row[2]
    
    # Create a Mol object from the SMILES string
    m = Chem.MolFromSmiles(smiles)
    m.SetProp('_Name', mol_name)

    # Create a drawer with a specified image size
    drawer = Draw.MolDraw2DCairo(200, 200)

    # Set the background color to transparent by setting the alpha channel to 0
    drawer.drawOptions().setBackgroundColour((1, 1, 1, 0))

    # Prepare and draw the molecule with a transparent background
    rdMolDraw2D.PrepareAndDrawMolecule(drawer, m)

    # Finish the drawing and convert it to an image
    drawer.FinishDrawing()
    img_data = drawer.GetDrawingText()

    # Save the image to a .png file named using the fileName variable
    with open(f"{CAS}noName.png", "wb") as img_file:
        img_file.write(img_data)