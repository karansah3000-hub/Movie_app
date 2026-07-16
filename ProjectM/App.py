import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import plotly.graph_objects as go
import time
from pathlib import Path

def get_base64_image(image_path):
      try:
         with open(image_path,"rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
      except FileNotFoundError:
         return ""
backgrounds = ["BG/bg1.jpg","BG/bg2.jpg","BG/bg3.jpg","BG/bg4.jpg","BG/bg5.jpg"] 
selected_background = random.choice(backgrounds)
background_base64 = get_base64_image(selected_background)
st.markdown(
    f"""
    <style>

    .stApp {{

        background-image:
            linear-gradient(
                rgba(0,0,0,0.80),
                rgba(0,0,0,0.80)
            ),
            url(
                "data:image/jpeg;base64,{background_base64}"
            );

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }}

    </style>
    """,
    unsafe_allow_html=True
)    

with st.spinner("🍿 Preparing cinematic insights..."):
   time.sleep(2)

st.set_page_config(page_title="Watch Craft", page_icon="🎬", layout="wide")
###########################################
st.markdown("""
<style>

.glass-card{
    background: rgba(
        255,
        255,
        255,
        0.06
    );

    backdrop-filter: blur(15px);

    border-radius:20px;

    padding:25px;

    border:1px solid rgba(
        255,
        255,
        255,
        0.15
    );

    transition:0.4s;
}

.glass-card:hover{
    transform:translateY(-8px);
    box-shadow:
    0px 0px 25px
    rgba(
        255,
        75,
        75,
        0.35
    );
}

</style>
""",unsafe_allow_html=True)
###########################################

###########################################

BASE_DIR = Path(__file__).resolve().parent
csv_path = BASE_DIR / "Movie.csv"

df = pd.read_csv(csv_path)
df.info()
with st.sidebar:
    st.image("BG/wlcm.gif")
    st.title("📋 DASHBOARD 📋")
    st.markdown("""
    <style>

    section[data-testid="stSidebar"]{
        background:
            linear-gradient(
                180deg,
                #0f0f0f,
                #171717,
                #202020
            );

        border-right:
            1px solid rgba(
                255,
                255,
                255,
                0.08
            );

        box-shadow:
            5px 0px 25px rgba(
                255,
                75,
                75,
                0.25
            );
    }

    section[data-testid="stSidebar"] *{
        color:white !important;
    }

    </style>
    """, unsafe_allow_html=True)
    opt=option_menu("Explore",options=["Home","Dataset","Pre-processing","Visualization","Insights","Movie Recommender","About"],icons=["house","file-text","activity","bar-chart","lightbulb","star","person"],default_index=0)
    st.divider()
    st.subheader("🎬 Movie Explorer")
    selected_movie = st.selectbox("Select a Movie",sorted(df["Title"].dropna().unique()))
    movie_data = df[df["Title"] == selected_movie].iloc[0]
    with st.expander("📖Click Here For Movie Details",expanded=False):
       st.write(f"## 🎥 {movie_data['Title']}")
       st.write(f"**🎬 Director:** {movie_data['Director']}")
       st.write(f"**📅 Year:** {movie_data['Year']}")
       st.write(f"**🎭 Genre:** {movie_data['Genre']}")
       st.write(f"**🌎 Language:** {movie_data['Language']}")
       st.write(f"**⭐ IMDb:** {movie_data['IMDb_100']}")
       st.write(f"**🍅 Critics:** {movie_data['Critic_Rating_RT']}")
       st.write(f"**👥 Audience:** {movie_data['Audience_Rating']}")
       if "Cast" in df.columns:
          st.write("### 🎭 Cast")
          cast_members = (movie_data["Cast"].split(","))
          for actor in cast_members:
             st.write(f"• {actor.strip()}")
       if "Plot" in df.columns:
          st.write("### 📖Plot")
          st.info(movie_data["Plot"])
               

if opt=="Home":
    # st.balloons()
    quotes=["😈Why so serious?😈","🌟May the Force be with you.🌟","🤖I am Iron Man.🤖","😉I'll be back.😉","🛸To infinity and beyond.♾️"]
    # st.subheader("Once a Legend Said😁:")
    st.title(random.choice(quotes),text_alignment="center")
    st.divider()
    ##############################################
    st.markdown("""
    <div class='hero-banner'>
    <h1>🎬 WATCH CRAFT</h1>
    <h3>Discover Cinema Through Data</h3>
    </div>
    """,unsafe_allow_html=True)

   
       
    banner_base64 = get_base64_image("posters/Ban.jpg")
    st.markdown(f"""
    <style>

    .hero-banner {{
        text-align:center;
        padding:120px 50px;
        border-radius:25px;

        background:
            linear-gradient(
                rgba(0,0,0,0.75),
                rgba(0,0,0,0.75)
            ),
            url("data:image/jpeg;base64,{banner_base64}");

        background-size:cover;
        background-position:center;
        background-repeat:no-repeat;

        box-shadow:
            0px 0px 40px rgba(
                255,
                75,
                75,
                0.25
            );
    }}

    .hero-banner h1 {{
        color:white;
        font-size:70px;
        margin-bottom:10px;
    }}

    .hero-banner h3 {{
        color:#d8d8d8;
        font-size:28px;
    }}

    </style>
    """, unsafe_allow_html=True)
    ##############################################
    st.markdown("""
    <style>

    [data-testid="metric-container"]{
        background-color:#1d1d1d;
        border-radius:15px;
        padding:20px;
        transition:0.3s;
    }

    [data-testid="metric-container"]:hover{
        transform:scale(1.05);
        border:1px solid #ff4b4b;
    }

    </style>
    """,unsafe_allow_html=True)
    ##############################################
    st.markdown("""
    <h2 class='typing'>
    💖💖💖Movies are not watched.
    They are experienced.💖💖💖💖💖💖
    </h2>
    """,unsafe_allow_html=True)

    st.markdown("""
    <style>

    .typing{
        overflow:hidden;
        white-space:nowrap;
        border-right:3px solid red;

        width:0;

        animation:
            typing 5s steps(40,end)
            forwards,
            blink .8s infinite;
    }

    @keyframes typing{
        from{width:0}
        to{width:100%}
    }

    @keyframes blink{
        50%{
            border-color:transparent;
        }
    }

    </style>
    """,unsafe_allow_html=True)
    ##############################################
    
    st.divider()
    st.title("🎉Welcome to WATCH CRAFT🎉",text_alignment="center")
    st.write("This is a Streamlit app that showcases a collection of movies with their ratings, genres, and other relevant information. The app allows users to explore the dataset, visualize various aspects of the movies, and learn more about the developers behind the project.")
    st.divider()
    st.subheader("🎭🎬🎥  Developer's Current Favourite  🎥🎬🎭:")
    st.write("Click on the movie below to see their official ROTTEN TOMATO page and explore more about them.")
    #####################################################################################################
    def get_base64_image(image_path):
       try:
          with open(image_path,"rb") as img_file:
             return base64.b64encode(img_file.read()).decode()
       except FileNotFoundError:
          return ""
       
    image_buttons={"posters/JW4.jpg":{"url": "https://www.rottentomatoes.com/m/john_wick_chapter_4", "title": "JOhn Wick: Chapter 4"},"posters/HTTYD.jpg":{"url": "https://www.rottentomatoes.com/m/how_to_train_your_dragon", "title": "How to Train Your Dragon"},"posters/OB.jpg":{"url": "https://www.rottentomatoes.com/m/obsession_2025", "title": "Obsession"},
                   "posters/EDB.jpg":{"url": "https://www.rottentomatoes.com/m/evil_dead_burn", "title": "Evil Dead Burn"},"posters/AIW.jpg":{"url": "https://www.rottentomatoes.com/m/avengers_infinity_war", "title": "Avengers: Infinity War"},"posters/GVK2.jpg":{"url": "https://www.rottentomatoes.com/m/godzilla_vs_kong", "title": "Godzilla v/s Kong"},
                   "posters/POTCAWE.jpg":{"url": "https://www.rottentomatoes.com/m/pirates_of_the_caribbean_3", "title": "Pirates Of The Caribbean"},"posters/PHM.jpg":{"url": "https://www.rottentomatoes.com/m/project_hail_mary", "title": "Project Hail Mary"},"posters/FRK.jpg":{"url": "https://www.rottentomatoes.com/m/frankenstein_2025", "title": "Frankenstein(2025)"}}

    hover_css="""
    <style>
    .img-button-container{ display: flex;gap: 30px;flex-wrap: wrap;padding: 15px 0;}
    .glow-img-btn{animation:float 4s ease-in-out infinite;}
    @keyframes float{0%{transform:translateY(0px);}50%{transform:translateY(-12px);}100%{transform:translateY(0px);}}
    .card-link {text-decoration: none !important;display: flex;flex-direction: column;align-items: center;width: 330px;}
    .glow-img-btn{width:350px;height:350px;object-fit:contain;cursor:pointer;border-radius:12px;border:2px solid transparent;transition:all 0.3s ease-in-out;}
    .btn-title {margin-top: 8px;font-size: 24px;font-weight: 500;color: #31333F; text-align: center;transition: color 0.3s ease;}
    .card-link:hover .glow-img-btn {border-color: #ff4b4b;box-shadow: 0 0 15px rgba(255, 75, 75, 0.6), 0 0 5px rgba(255, 75, 75, 0.4);transform: scale(1.03);}
    .card-link:hover .btn-title {color: #ff4b4b;}
    @media (prefers-color-scheme: dark) {.btn-title {color: #FAFAFA;}
    }
    </style>
    """  
    html_content = hover_css + '<div class="img-button-container">'
    for img_path, info in image_buttons.items():
       img_base64=get_base64_image(img_path)
       if img_base64:
          html_content +=(
             f'<a class="card-link" href="{info["url"]}" target="_blank">'
             f'  <img class="glow-img-btn" src="data:image/png;base64,{img_base64}">'
             f'  <div class="btn-title">{info["title"]}</div>'
             f'</a>')
    html_content += '</div>'  

    st.markdown(html_content,unsafe_allow_html=True)


elif opt=="Dataset":
     st.title("📂Original Dataset:")
     st.divider()
     st.markdown("""
     <div style='text-align:center; padding:10px;'>
         <h3 style='color:#FFD700;'>
             🍿 Every visualization starts with a story hidden in the data.
             Explore the foundation of Watch Craft here.
         </h3>
     </div>
     """, unsafe_allow_html=True)
     st.divider()
     col1,col2,col3,col4,col5,col6=st.columns(6)
     with col1:
      st.metric("🎬 Movies",len(df))
     with col2:
      st.metric("🎭 Genres",df["Genre"].str.get_dummies(sep=", ").shape[1])
     with col3:
      st.metric("⭐ Avg IMDb",round(df["IMDb_100"].mean(),2))
     with col4:
      st.metric("🍅 Avg Critics",round(df["Critic_Rating_RT"].mean(),2))
     with col5:
      st.metric("👥 Avg Audience",round(df["Audience_Rating"].mean(),2))
     with col6:
      top_genre=(df["Genre"].str.split(", ").explode().value_counts().idxmax())
      st.metric("🔥 Top Genre",top_genre)
     st.divider()

     t1,t2,t3=st.tabs(["Data","Info","Description"])
     with t1:
        st.dataframe(df,hide_index=True)
     with t2:
        st.write("Columns present in the Original Dataset")
        columns_df = pd.DataFrame({"Index": range(1, len(df.columns)+1),"Column Name": df.columns})
        st.dataframe(columns_df,use_container_width=True,hide_index=True)
     with t3:
        st.table(df.describe())

elif opt=="Pre-processing":
    st.title("⚙️Pre-Processing:")
    st.divider()
    st.markdown("""
    <div style='text-align:center; padding:10px;'>
        <h3 style='color:#2FD2EB;'>
            🍿 Welcome to the editing room of Watch Craft —
            where raw movie data gets its final cut before taking the spotlight.
        </h3>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    t1,t2=st.tabs(["Before-Processing","After-Processing"])
    with t1:
        columns_df = pd.DataFrame({"Index": range(1, len(df.columns)+1),"Column Name": df.columns,"Null Values":df.isna().sum()})
        st.dataframe(columns_df,use_container_width=True,hide_index=True)
    with t2:
        df.drop(columns=["Awards","Production","RT_URL","Audience_Reviews","Letterboxd_Votes","imdbID","Critic_Reviews","IMDb_Votes","IMDb_10"],inplace=True)
        df.dropna(inplace=True)
        df.reset_index(drop=True,inplace=True)
        df["Language"]=df["Language"].replace({"en":"English","ja":"Japanese","fr":"French","es":"Spanish","it":"Italian","de":"German","ko":"Korean","zh":"Chinese","da":"Danish","tr":"Turkish"},inplace=True)
        columns_df = pd.DataFrame({"Index": range(1, len(df.columns)+1),"Column Name": df.columns,"Null Values":df.isna().sum()})
        st.dataframe(columns_df,use_container_width=True,hide_index=True)
        st.dataframe(df)

elif opt=="Visualization":

    st.title("📊Data Visualization:")
    st.divider()
    st.subheader("🍿 Every movie tells a story. Our visualizations reveal the ones hidden in the data.")
   #  st.caption("🎥 From ratings and genres to streaming trends and hidden gems — discover cinema through the power of visualization.")
    st.markdown("""
    <div style='text-align:center; padding:10px;'>
        <h3 style='color:#27F52E;'>
            🎥 From ratings and genres to streaming trends and hidden gems —
            discover cinema through the power of visualization.
        </h3>
    </div>
    """, unsafe_allow_html=True)
    st.divider()

    viz1,viz2,viz3,viz4,viz5,viz6 = st.tabs([
        "🎯 Dashboard",
        "⭐ Ratings Explorer",
        "🎭 Genre Intelligence",
        "📺 Streaming Analytics",
        "🎬 Industry Insights",
        "💎 Hidden Gems"
    ])

    # Dashboard
    with viz1:
        st.subheader("Platform Overview")
        col1,col2,col3,col4,col5=st.columns(5)
        col1.metric("Movies",len(df))
        col2.metric("Genres",df["Genre"].str.get_dummies(sep=", ").shape[1])
        col3.metric("Avg IMDb",round(df["IMDb_100"].mean(),1))
        col4.metric("Directors",df["Director"].nunique())
        col5.metric("Languages",df["Language"].nunique())
        st.divider()
        metric = st.selectbox("Select Rating Metric",["IMDb_100","Audience_Rating","Critic_Rating_RT","Flickmetrix_Score","Letterboxd"])
        metric_names = {"IMDb_100": "IMDb","Audience_Rating": "Audience","Critic_Rating_RT": "Critics","Flickmetrix_Score": "Flickmetrix","Letterboxd": "Letterboxd"}

        fig = go.Figure(go.Indicator(mode="gauge+number+delta",value=df[metric].mean(),delta = {'reference':80},title={"text": f"Average {metric_names[metric]} Score"},gauge={"axis": {"range": [0,100]},"bar": {"color": "silver"},"steps": [{"range": [0,20], "color": "#330101"},{"range": [20,40], "color": "#8B0000"},{"range": [40,60], "color": "#FF0084"},{"range": [60,80], "color": "#C300FF"},{"range": [80,100], "color": "#32CD32"}]}))
        st.plotly_chart(fig,use_container_width=True)

        top_n = st.slider("Top Movies",5,30,15)
        top_movies = df.nlargest(top_n,metric)
        figgg = px.bar(top_movies,x=metric,y="Title",orientation="h",color=metric,hover_data=["Director","Year","Genre"])
        st.plotly_chart(figgg,use_container_width=True)

    with viz2:
        st.subheader("Ratings Explorer")

        fig = px.scatter(df,x="Critic_Rating_RT",y="Audience_Rating",size="IMDb_100",color="IMDb_100",hover_name="Title",title="Critics vs Audience")
        st.plotly_chart(fig,use_container_width=True)

        metric2 = st.selectbox("Rating Distribution",["IMDb_100","Audience_Rating","Critic_Rating_RT"])
        fig = px.histogram(df,x=metric2,nbins=20,title="Distribution",hover_data=["Director","Year","Genre"])
        st.plotly_chart(fig,use_container_width=True)

        ratings_long = df.melt(value_vars=["IMDb_100","Audience_Rating","Critic_Rating_RT","Flickmetrix_Score","Letterboxd"],var_name="Platform",value_name="Score")
        fig = px.box(ratings_long,x="Platform",y="Score",color="Platform")
        st.plotly_chart(fig)

        fig = px.violin(ratings_long,x="Platform",y="Score",box=True)
        st.plotly_chart(fig)

    with viz3:
        genre_dummies = df["Genre"].str.get_dummies(sep=", ")
        df = pd.concat([df, genre_dummies], axis=1)
        df["Genre_List"]=df["Genre"].str.split(", ")
        Drama_movies=df[df["Drama"]==1]
        Action_movies=df[df["Action"]==1]
        Adventure_movies=df[df["Adventure"]==1]
        Animation_movies=df[df["Animation"]==1]
        Comedy_movies=df[df["Comedy"]==1]
        Crime_movies=df[df["Crime"]==1]
        Documentary_movies=df[df["Documentary"]==1]
        Family_movies=df[df["Family"]==1]
        Fantasy_movies=df[df["Fantasy"]==1]
        History_movies=df[df["History"]==1]
        Horror_movies=df[df["Horror"]==1]
        Music_movies=df[df["Music"]==1]
        Mystery_movies=df[df["Mystery"]==1]
        Romance_movies=df[df["Romance"]==1]
        Sci_Fi_movies=df[df["Science Fiction"]==1]
        Thriller_movies=df[df["Thriller"]==1]
        War_movies=df[df["War"]==1]
        Western_movies=df[df["Western"]==1]
        ####################################################################################################
        
        #####################################################################################################


        st.title("Movies by Genre Distribution")
        genre_cols = ['Action','Adventure','Animation','Comedy','Crime','Documentary','Drama','Family','Fantasy','History','Horror','Music','Mystery','Romance','Science Fiction','Thriller','War','Western']
        genre_counts = (df[genre_cols].sum().sort_values(ascending=False).reset_index())
        genre_counts.columns = ["Genre", "Movies"]
        fig1= px.line(genre_counts,x="Genre",y="Movies",color_discrete_sequence=px.colors.qualitative.Set1,markers=True,title="Genre Distribution",labels={"Movies": "Number of Movies"})
        fig1.update_layout(xaxis_tickangle=-45)
        with st.container(border=True):
            st.plotly_chart(fig1)
        genre_dummies = df["Genre"].str.get_dummies(sep=", ")
        genre_counts = genre_dummies.sum().sort_values(ascending=False).reset_index()
        genre_counts.columns=["Genre","Movies"]

        fig = px.treemap(genre_counts,path=["Genre"],values="Movies")
        st.plotly_chart(fig,use_container_width=True)

        genre_heat = pd.DataFrame({"Genre":genre_cols,"IMDb":[df[df[g]==1]["IMDb_100"].mean() for g in genre_cols],"Audience":[df[df[g]==1]["Audience_Rating"].mean() for g in genre_cols],"Critics":[df[df[g]==1]["Critic_Rating_RT"].mean() for g in genre_cols]})
        fig = px.imshow(genre_heat.set_index("Genre"),text_auto=".1f",aspect="auto")
        st.plotly_chart(fig,use_container_width=True)

        fig = px.sunburst(genre_counts,path=["Genre"],values="Movies")
        st.plotly_chart(fig)

    with viz4:
        streaming_dummies = df["Streaming_On"].str.get_dummies(sep=", ")
        df = pd.concat([df, streaming_dummies], axis=1)
        df["Stream_List"]=df["Streaming_On"].str.split(", ")
        platform_cols = ["amzvid","apple","britbox","disney","hbm","hbo","hulu","itunes","mubi","netflix","paramount","peacock","prime","starz"]
        platform_names = {"amzvid":"Amazon Prime Video","apple":"Apple TV+","britbox":"BritBox","disney":"Disney+","hbm":"HBO Max","hbo":"HBO","hulu":"Hulu","itunes":"iTunes","mubi":"MUBI","netflix":"Netflix","paramount":"Paramount+","peacock":"Peacock","prime":"Prime Video","starz":"Starz"}
        platform_counts = (df[platform_cols].sum().reset_index())
        platform_counts.columns = ["Platform","Movies"]
        platform_counts["Platform"] = (platform_counts["Platform"].map(platform_names))
        platform_compare = pd.DataFrame({"Platform": [platform_names[p]for p in platform_cols],"IMDb": [df[df[p] == 1]["IMDb_100"].mean()for p in platform_cols],"Audience": [df[df[p] == 1]["Audience_Rating"].mean()for p in platform_cols],"Critics": [df[df[p] == 1]["Critic_Rating_RT"].mean()for p in platform_cols],"Flickmetrix": [df[df[p] == 1]["Flickmetrix_Score"].mean()for p in platform_cols],"Letterboxd": [df[df[p] == 1]["Letterboxd"].mean()for p in platform_cols]})

        fig = px.pie(platform_counts,names="Platform",values="Movies",hole=.45)
        st.plotly_chart(fig,use_container_width=True)

        fig = px.scatter(platform_compare,x="Critics",y="Audience",size="IMDb",color="Platform")
        st.plotly_chart(fig)
        platform_compare = pd.DataFrame({"Platform":[platform_names[p]for p in platform_cols],"IMDb":[df[df[p]==1]["IMDb_100"].mean()for p in platform_cols],"Audience":[df[df[p]==1]["Audience_Rating"].mean()for p in platform_cols],"Critics":[df[df[p]==1]["Critic_Rating_RT"].mean()for p in platform_cols]})  
        comparison_long = platform_compare.melt(id_vars="Platform",var_name="Metric",value_name="Score")
        fig = px.line_polar(comparison_long,r="Score",theta="Platform",color="Metric",line_close=True,title="Platform's Rating distribution")
        st.plotly_chart(fig)

        fig = px.imshow(platform_compare.set_index("Platform"),text_auto=".1f",aspect="auto",title="Platform's Rating distribution")
        st.plotly_chart(fig)

        matrix=[]

        for platform in platform_cols:
            row=[]
            for genre in genre_cols:
                row.append(
                    len(
                        df[
                            (df[platform]==1) &
                            (df[genre]==1)
                        ]
                    )
                )
            matrix.append(row)

        matrix = pd.DataFrame(
            matrix,
            index=[platform_names[p] for p in platform_cols],
            columns=genre_cols
        )

        fig = px.imshow(matrix,text_auto=True,title="Platform's Genre distribution")

        st.plotly_chart(fig)

    with viz5:
        movies_year = df.groupby("Year").size().reset_index(name="Movies")

        fig = px.line(movies_year,x="Year",y="Movies",markers=True,title="Movies Released per year(According to dataset)")
        st.plotly_chart(fig,use_container_width=True)

        corr = df.select_dtypes(include="number").corr()
        fig = px.imshow(corr,text_auto=".2f",color_continuous_scale="RdBu_r",aspect="auto",title="Correlations")
        st.plotly_chart(fig,use_container_width=True)

        df["Decade"] = (df["Year"]//10)*10
        fig = px.histogram(df,x="Decade",color="Decade",title="Movies distribution by year")
        st.plotly_chart(fig)

        trend = df.groupby("Year")["IMDb_100"].mean().reset_index()
        fig = px.line(trend,x="Year",y="IMDb_100",markers=True,title="Average IMDb distribution by year")
        st.plotly_chart(fig)

        df["Language"]=df["Language"].replace({"en":"English","ja":"Japanese","fr":"French","es":"Spanish","it":"Italian","de":"German","ko":"Korean","zh":"Chinese(Traditional)","da":"Danish","tr":"Turkish","pt":"Portuguese","fa":"Farsi(Persian)","sv":"Swedish","no":"Norwegian","pl":"Polish","cn":"Chinese(Standard)"},inplace=True)
        lang = (df["Language"].value_counts().reset_index())
        fig = px.pie(lang,names="Language",values="count",hole=0.45,title="Language Distribution")
        st.plotly_chart(fig)

    with viz6:
       st.title("💎 Hidden Gem Detector")

       st.write("💸💸  Find highly rated movies that deserve more attention.  💸💸")
       if st.button("💎 Discover Hidden Gems"):
            hidden_gems = df[(df["IMDb_100"]>=85) &(df["Audience_Rating"]>=85) &(df["Critic_Rating_RT"]>=75)].sample(10)
            st.dataframe(hidden_gems[["Title","Director","Genre","IMDb_100","Audience_Rating"]])
       hidden_gems = df[(df["IMDb_100"] >= 85) &(df["Audience_Rating"] >= 85) &(df["Critic_Rating_RT"] >= 80) &(df["Flickmetrix_Score"] >= 85)]
       if st.button("🎰 Spin Movie Wheel"):

        st.toast(
            "🎥 Rolling the reels..."
        )

        progress = st.progress(0)

        placeholder = st.empty()

        for i in range(30):

            movie = random.choice(
                hidden_gems["Title"].tolist()
            )

            placeholder.markdown(
                f"# 🎰 {movie}"
            )

            progress.progress(
                int((i+1)/30*100)
            )

            time.sleep(0.08)

        winner = hidden_gems.sample(1).iloc[0]

        st.balloons()

        placeholder.success(
            f"""
            # 🎬 {winner['Title']}

            ⭐ IMDb: {winner['IMDb_100']}

            🍿 Audience: {winner['Audience_Rating']}

            🍅 Critics: {winner['Critic_Rating_RT']}
            """
        ) 

elif opt=="Insights":
    st.title("👁️Insights")
    st.divider()
    st.markdown("""
    <div style='text-align:center; padding:10px;'>
        <h3 style='color:#F584E8;'>
            🍿 Welcome to the director's commentary of Watch Craft —
            where data speaks and cinema reveals its secrets.
        </h3>
    </div>
    """, unsafe_allow_html=True)
    top_genre=(df["Genre"].str.split(", ").explode().value_counts().idxmax())
    st.divider()
    col1,col2,col3,col4=st.columns(4)

    col1.metric("🎬Movies",len(df))
    col2.metric("🍿Avg IMDb",round(df["IMDb_100"].mean(),2))
    col3.metric("🔥 Top Genre",top_genre)
    col4.metric("🎥Top Movie",df.iloc[0]["Title"])
    
    st.divider()
    st.title("💡 Movie Insights")
    top_genre=(df["Genre"].str.split(", ").explode().value_counts().idxmax())
    best_movie=df.loc[df["IMDb_100"].idxmax()]["Title"]
    best_director=(df.groupby("Director")["IMDb_100"].mean().idxmax())
   #  best_language=(df.groupby("Language")["IMDb_100"].mean().idxmax())
    decade=((df["Year"]//10)*10)
    best_decade=(decade.value_counts().idxmax())
    c1,c2=st.columns(2)
    with c1:
        st.success(f"🎭 Most Popular Genre: {top_genre}")
        st.info(f"⭐ Highest Rated Movie: {best_movie}")
        st.success(f"🎬 Best Director: {best_director}")
        st.info("""
                   🌟The dataset is heavily biased toward excellent movies:

                   👉🏻Lowest IMDb score is still 71/100\n
                   👉🏻Lowest Custom Score is 77\n
                   👉🏻Highest Custom Score reaches 93.83\n

                   →→→This indicates the dataset likely contains curated top films rather than the entire movie industry
                   """)
        st.success("""
                   🌟Language Distribution:\n

                   👉🏻Around 74% of the movies are in English.\n
                   👉🏻Japanese cinema has the strongest international presence after English films.\n
                   👉🏻 Korean cinema is represented despite having far fewer historical releases, showing its rapidly growing global influence.\n

                   """)
        st.info("""
                   🌟Director Analysis:\n

                   👉🏻Directors with highly recognizable visual styles dominate the rankings.\n
                   👉🏻JAuteur filmmakers are heavily favored by critics and movie enthusiasts.\n
                   👉🏻 Hayao Miyazaki's presence among live-action legends highlights animation's growing critical importance.\n

                   """)
    with c2:
        st.info(f"🌎 Best Language: English")
        st.success(f"📅 Best Decade: {best_decade}s")
        st.info(f"🎥 Total Directors: {df['Director'].nunique()}")
        st.success("""
                 🌟Genre Analysis:\n
                👉🏻Nearly 66% of all movies contain the Drama genre.\n
                👉🏻Action and Sci-Fi are significantly underrepresented compared to Drama.\n
                👉🏻Critics and ranking systems tend to favor dramatic storytelling over spectacle-driven films.\n

                """)
        st.info("""
                 🌟Release Year Trends:\n
                👉🏻The 2010s dominate the dataset, suggesting recent films are increasingly receiving critical recognition.\n
                👉🏻The rise may be due to:\n
                      → Global streaming platforms\n
                      → Greater international accessibility\n
                      → Increased audience participation in online rating systems\n
                
                """)
    st.warning("""
                  🎥🎥🎥🎥🎥🎥   FINAL CONCLUSION   🎥🎥🎥🎥🎥🎥

👉🏻 This dataset represents a collection of ELITE CINEMA rather than average cinema.

👉🏻 The ideal movie in this dataset tends to be:

• A DRAMA or THRILLER,\n
• Released after 2000,\n
• Directed by an acclaimed auteur filmmaker,\n
• STRONGLY RATED by both critics and audiences,\n
• Popular enough to gather substantial reviews but not necessarily blockbuster-level viewership.\n

👉🏻 The analysis shows that critical quality and audience appreciation align much more strongly with movie rankings than raw popularity metrics such as vote counts or review volume.
               """)
       
elif opt=="Movie Recommender":
   st.title("🎬Movie Recommender System")
   st.write("this page is currently under development.")
   col1,col2=st.columns(2)
   with col1:
      st.image("BG/CS.gif") 
   with col2:
      st.image("BG/hardwrk.gif") 

elif opt=="About":
    st.title("🙋🏻‍♂️About:")
    st.divider()
    st.markdown("""
    <div style='text-align:center; padding:10px;'>
        <h3 style='color:#87327F;'>
            🎥 Behind every chart, insight, and recommendation lies a passion for cinema and the art of storytelling.
        </h3>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown("""
    <div style="
        text-align:center;
        padding:20px;
        border-radius:20px;
        background: linear-gradient(135deg,#141E30,#243B55);
        color:white;
    ">
        <h1>🎬 WATCH CRAFT</h1>
        <h3 style="color:#FFD700;">
            Discover Cinema Through Data
        </h3>
    </div>
    """,unsafe_allow_html=True)

    st.write("")

    col1,col2=st.columns(2)
    with col1:
        st.info("""
### 🎯 Project Objective

Watch Craft transforms raw movie datasets into an immersive analytics experience.

Instead of browsing spreadsheets, users can interact with visual dashboards, explore trends, compare ratings, and discover hidden cinematic gems.
""")
        fun_facts = ["🔮FUN-FACT:  \n🍿 The average person spends over 5 years of their life watching movies and TV shows.","🔮FUN-FACT:  \n🎥 Watch Craft analyzes cinema using five different rating systems simultaneously.","🔮FUN-FACT:  \n🎭 The same movie can be loved by audiences and disliked by critics.","🔮FUN-FACT:  \n📊 Every visualization in Watch Craft begins as raw movie data.","🔮FUN-FACT:  \n🎬 The first public movie screening happened in Paris in 1895."]
        st.info(random.choice(fun_facts))
    with col2:
        st.success("""
### 🚀 Key Features

🎥 Explore Movie Datasets

📊 Interactive Visualizations

⭐ Multi-platform Rating Analysis

📺 Streaming Platform Insights

💎 Hidden Gem Detector

🎭 Genre Analytics

🔍 Movie Explorer Panel
""")

    st.divider()
    st.markdown("""
## 🛠 Technologies Used
""")

    tech1,tech2,tech3=st.columns(3)
    with tech1:
        st.metric("🐍 Python","100%")
    with tech2:
        st.metric("⚡ Streamlit","Frontend")
    with tech3:
        st.metric("📈 Plotly","Visualization")
    st.write("")
    st.markdown("""
<div style="
padding:20px;
border-radius:15px;
background-color:#1E1E1E;
border-left:5px solid #FF4B4B;
">
<h2 style="color:#FF4B4B;">🎬 Why Watch Craft?</h2>
<p style="font-size:18px;color:#E0E0E0;">
Movies are more than entertainment — they reflect cultures,
stories, emotions, and audience preferences.
</p>
<p style="font-size:18px;color:#00C9A7;">
Watch Craft combines the power of Data Science and Cinema
to make movie exploration more immersive and insightful.
</p>
</div>
""",unsafe_allow_html=True)

    st.write("")

    st.markdown("""
<div style="
text-align:center;
padding:25px;
border-radius:20px;
background: linear-gradient(90deg,#232526,#414345);
">
<h2 style="color:#FFD700;">
👨‍💻 Developed By
</h2>
<h3 style="color:white;">
Karan Sah
</h3>
<p style="color:#B0B0B0;">
Python • Data Science • Streamlit • Plotly
</p>
<h4 style="color:#FF4B4B;">
🍿 "Movies are not just watched.
They are experienced."
</h4>
</div>
""",unsafe_allow_html=True)          
#################################################
st.markdown("""
<hr>
<center>
Built with ❤️ and 🍿 using
Python, Streamlit and Plotly.

WATCH CRAFT © 2026
</center>
""",unsafe_allow_html=True)