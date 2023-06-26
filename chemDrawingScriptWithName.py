import csv
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import rdMolDraw2D

csv_file = 'yourCSVFileName.csv'

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

    # Configure drawing options to include atom indices and molecule name
    drawing_options = Draw.MolDrawOptions()
    drawing_options.includeAtomNumbers = True
    drawing_options.legendFontSize = 15
    drawing_options.padding = 0.05

    # Create a drawer with a specified image size
    drawer = Draw.MolDraw2DCairo(200, 200)
    drawer.SetDrawOptions(drawing_options)

    # Set the background color to transparent by setting the alpha channel to 0
    drawer.drawOptions().setBackgroundColour((1, 1, 1, 0))

    # Prepare and draw the molecule with a transparent background
    rdMolDraw2D.PrepareAndDrawMolecule(drawer, m, legend=mol_name)

    # Finish the drawing and convert it to an image
    drawer.FinishDrawing()
    img_data = drawer.GetDrawingText()

    # Save the image to a .png file named using the fileName variable
    with open(f"{CAS}withName.png", "wb") as img_file:
        img_file.write(img_data)
