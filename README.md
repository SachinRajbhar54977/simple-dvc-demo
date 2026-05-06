
   2 conda create -n wineq python=3.10 -y                                                                                                        
   3 conda update -n base -c defaults conda                                                                                                      
   4 conda activate wineq                                                                                                                        
   5 in requirements.txt                                                                                                                         
   6 ni requirements.txt                                                                                                                         
   7 pip install requirements.txt                                                                                                                
   8 pip install requirements.txt                                                                                                                
   9 pip install -r requirements.txt                                                                                                             
  10                                                                                                                                         
  11 pip install -r requirements.txt                                                                                                             
  12                                                                                                                                       
  13 ni README.md    


  git init 
  dvc init
  dvc add data data_given/wineq

  git add  .
  git commit -m "first commit"
  

    75 mkdir report                                                                                                                                
  76 ni report/params.json                                                                                                                       
  77 ni report/scores.json                                                                                                                       
  78 dvc repro                                                                                                                                   
  79 dvc metrics show                                                                                                                            
  80 dvc metrics diff                                                                                                                            

  