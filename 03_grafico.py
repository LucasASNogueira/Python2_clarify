import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go 


# Dicionarios com as informações da caixa dropdown
dados_conceitos = {
    'java':{'Variaveis': 8, 'Condicionais': 10, 'Loops': 4, 'poo': 3, 'funções': 4},

    'python':{'Variaveis': 9, 'Condicionais': 7, 'Loops': 8, 'poo': 3, 'funções': 7},
    
    'sql':{'Variaveis': 10, 'Condicionais': 9, 'Loops': 1, 'poo': 5, 'funções': 4},
    
    'golang':{'Variaveis': 6, 'Condicionais': 15, 'Loops': 2, 'poo': 3, 'funções': 1},
    
    'javascript':{'Variaveis': 1, 'Condicionais': 10, 'Loops': 4, 'poo': 8, 'funções': 4}

}

cores_map = dict(
    java = 'red',
    python = 'green',
    sql = 'yellow',
    golang = 'blue',
    javaspript = 'pink'

)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H4('Cursos de TI', style={'textAlign': 'center'}),
    html.Div(
        dcc.Dropdown(
            id='dropdown_linguagens',
            options=[
                {'label':'Java', 'value': 'java'},
                {'label':'Python', 'value': 'python'},
                {'label':'SQL', 'value': 'sql'},
                {'label':'GoLang', 'value': 'golang'},
                {'label':'JavaScript', 'value': 'javascript'}
            ], 
            value='java',
            multi=True,
            style={'width': '50%', 'margin': '0 auto', 'textAlign': 'center'}

        )
    ),
    dcc.Graph(
        id='grafico_linguagem'
        )
], style={'width': '80%', 'margin': '0 auto'}
)

# Uma função que vai chamar através do evento 
@app.callback(
    Output('grafico_linguagem', 'figure'),
    [Input('dropdown_linguagens', 'value')]
)

def scarter_linguagens(linguagens_selecionadas):
    scarter_trace = []

    for linguagem in linguagens_selecionadas:
        dados_linguagem = dados_conceitos[linguagem]
        for conceito, conhecimento in dados_linguagem.items():
            scarter_trace.append(
                go.Scatter(
                    x=[conceito],
                    y=[conhecimento],
                    mode = 'markers',
                    name=linguagem.title(),
                    marker=dict(
                        size=15,
                        color=cores_map[linguagem],
                   showlegend=False
                    )
                )
            )
    scarter_layout = go.layout(
        title="Meus conhecimentos em Linguagens de Programação",
        xaxis=dict(title = 'Conceitos', showgrid=False),
        yaxis=dict(title = 'Niveis de Conhecimento', showgrid=False) 
    )

    return {'data':scarter_trace, 'layout': scarter_layout}

if __name__ == '__main__':
    app.run_server(debug=True)
