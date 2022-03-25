# CCU Dashboard

## How to run
1. Open two terminals. [How to split terminals using Visual Studio Code](https://code.visualstudio.com/updates/v1_21#_split-terminals)
2. In the first terminal navigate to "ccu-dashboard/frontend" and run the command "npm run dev".
3. In the second terminal navigate to "ccu-dashboard/new-backend" and run the command "python3 app.py".
4. If successful you can open http://localhost:3000 and view the website. 

## How to setup
### Frontend

1. Check you have npm installed. If not follow this guide [How to Install npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
2. Navigate to "ccu-dashboard/frontend" folder.
3. Next run "npm install".
4. Check you have element plus installed. If not run the command "npm install element-plus --save".
5. Also install the following using npm. "npm install -D unplugin-vue-components unplugin-auto-import".

### Backend

1. Install the requirements using pip. "pip install flask Werkzeug".
2. Create a folder named "temp" in "ccu-dashboard/new-backend" if one does not already exist.
3. Run app.py. This can be done for example by doing "python3 app.py". 


