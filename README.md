# Renal Cell Carcinoma and Kidney Segmentation using nnUNet
Renal Cell carcinoma is the most common malignant tumor arising from kidneys, largely incurable and resistant to conventional chemotherapy.
There has been development of novel anticancer agents to work upon such cancers. One such anticancer agent is Tyrosine Kinase Inhibitors (TKI). TKI is the only approved therapy in patients that are not candidates for immunotherapy. So the aim of this project is to evaluate radiological tumor response of TKI in patients with advanced RCC after chemotherapy by performing automated semantic segmentation in CT imaging of these tumors from their corresponding kidneys using Deep Learning and to assist the study of correlating the immunophenotype and the type of RCC based on radiographic features.

A pubicly available dataset "kits19" has been used in this project available at "https://github.com/neheller/kits19". Follow the instructions on this page to acquire the dataset.

The primary aim of this project is to correlate the immunophenotype  with the type of RCC based on radiographic features for which a private dataset was supposed to be acquired.
The sate-of-the-art network architecture nnUNet for automated biomedical semantic segmentation available at "https://github.com/MIC-DKFZ/nnUNet" was used to acquire the segmentation of tumors.

The main folder contains files required and used to meet the format of nnUNet. These files were created upon facing a few issues in re-implemenatation of nnUNet model.
Link to the issues are as follows:
        https://github.com/MIC-DKFZ/nnUNet/issues/172
        
