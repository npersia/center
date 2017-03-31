from bottle import route, default_app, template, run, static_file, error
import weather
import subte

@route('/')
def index():
    
    weather_icon = "1483398180_weather-01.png"
    temp = "27"
    lugar = "Parque Chacabuco, Buenos Aires"
    estado_clima = "Soleado"
    #prob_lluvia = "15"
    porc_humedad = "30"
    vel_viento = "23"
    
    weatherResp = weather.getWeather("-34.5638807","-58.4620623,17")
    
    weather_icon = weatherResp["icon"]
    temp = weatherResp["temp"]
    lugar = weatherResp["city"]
    estado_clima = weatherResp["weather"]
    #prob_lluvia = "15"
    porc_humedad = weatherResp["hum"]
    vel_viento = weatherResp["wind"]

    subteResp = subte.getSubte()


    estado_linea_a = subteResp["linea_a"]["estado"]
    estado_linea_b = subteResp["linea_b"]["estado"]
    estado_linea_c = subteResp["linea_c"]["estado"]
    estado_linea_d = subteResp["linea_d"]["estado"]
    estado_linea_e = subteResp["linea_e"]["estado"]
    estado_linea_h = subteResp["linea_h"]["estado"]
    estado_linea_p = subteResp["linea_p"]["estado"]
    estado_linea_u = subteResp["linea_u"]["estado"]
    color_estado_subte_a = subte.getColorStatus(estado_linea_a)
    color_estado_subte_b = subte.getColorStatus(estado_linea_b)
    color_estado_subte_c = subte.getColorStatus(estado_linea_c)
    color_estado_subte_d = subte.getColorStatus(estado_linea_d)
    color_estado_subte_e = subte.getColorStatus(estado_linea_e)
    color_estado_subte_h = subte.getColorStatus(estado_linea_h)
    color_estado_subte_p = subte.getColorStatus(estado_linea_p)
    color_estado_subte_u = subte.getColorStatus(estado_linea_u)



    return template("/myfiles/page/center.html",\
t_weather_icon=weather_icon,\
t_temp=temp,\
t_lugar=lugar,\
t_estado_clima=estado_clima,\
t_porc_humedad=porc_humedad,\
t_vel_viento=vel_viento,\
t_estado_linea_a=estado_linea_a,\
t_estado_linea_b=estado_linea_b,\
t_estado_linea_c=estado_linea_c,\
t_estado_linea_d=estado_linea_d,\
t_estado_linea_e=estado_linea_e,\
t_estado_linea_h=estado_linea_h,\
t_estado_linea_p=estado_linea_p,\
t_estado_linea_u=estado_linea_u,\
t_color_estado_subte_a=color_estado_subte_a,\
t_color_estado_subte_b=color_estado_subte_b,\
t_color_estado_subte_c=color_estado_subte_c,\
t_color_estado_subte_d=color_estado_subte_d,\
t_color_estado_subte_e=color_estado_subte_e,\
t_color_estado_subte_h=color_estado_subte_h,\
t_color_estado_subte_p=color_estado_subte_p,\
t_color_estado_subte_u=color_estado_subte_u\
)


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/myfiles/static')

@error(404)
def error404(error):
    return 'Nothing here, sorry'

run(host='0.0.0.0', port=8000)
