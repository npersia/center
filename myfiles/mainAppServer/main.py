from bottle import route, default_app, template, run, static_file, error
import weather

@route('/')
def index():
    
    weather_icon = "1483398180_weather-01.png"
    temp = "27"
    lugar = "Parque Chacabuco, Buenos Aires"
    estado_clima = "Soleado"
    prob_lluvia = "15"
    porc_humedad = "30"
    vel_viento = "23"
    
    weatherResp = weather.getWeather("-34.6421149","-58.4612144")
    
    weather_icon = weatherResp["icon"]
    temp = weatherResp["temp"]
    lugar = weatherResp["city"]
    estado_clima = weatherResp["weather"]
    prob_lluvia = "15"
    porc_humedad = "30"
    vel_viento = weatherResp["wind"]
    
    return template("./page/center.html",t_weather_icon=weather_icon,t_temp=temp,t_lugar=lugar,t_estado_clima=estado_clima,t_prob_lluvia=prob_lluvia,t_porc_humedad=porc_humedad,t_vel_viento=vel_viento)


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@error(404)
def error404(error):
    return 'Nothing here, sorry'

run(host='0.0.0.0', port=8000)
