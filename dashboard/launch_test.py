
#%%
%%sh
# Get ngrok
curl -O https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip ngrok-stable-linux-amd64.zip

#%%

# Launch ngrok
get_ipython().system_raw('./ngrok http 8050 &')

#%%

%%sh
# Get url with ngrok
curl -s http://localhost:4040/api/tunnels | python3 -c "import sys, json; print(json.load(sys.stdin)['tunnels'][0]['public_url'])"

#%%

#Run the dash app
!python dash_app.py