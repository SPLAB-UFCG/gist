package Exemplos.SimpleServer;

import static spark.Spark.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ConnectException;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
/**
 * Hello world!
 *
 *
 *Simulação de um Web server simples, simulando duas rotas GET em repositorios
 *em usuários e repositorios públicos, processando o objeto json e demonstrando
 * informações no navegador. Utilizando da framework Spark java, e a biblioteca
 * externa simple json para processamento de objetros json 
 *
 */
public class App 
{
    public static void main( String[] args ) throws ParseException, IOException
    {	
		/**
		 * primeira rota GET, na qual é passada pelo parâmetro o nome do usuário
		 * e é retornada informações do usuário
		 * Então o objeto json retornado pela API do git é processada
		 * a página entao é estruturada para ser retornada para o navegador
		*/
    	get("user/:name", (req, res) -> { 
    		String rawJson = recuperaUser(req.params(":name"));
    		Object obj = new JSONParser().parse(rawJson);
    		JSONObject jo = (JSONObject) obj;
    		return  pageUser(jo);
    		});
    	/**
		 * segunda rota GET, na qual é passada pelo parâmetro o nome do usuário e o repositorio
		 * São então retornadas as informações sobre o repositorio em um objeto JSON
		 * Então o objeto json retornado pela API do git é processada
		 * a página entao é estruturada para ser retornada para o navegador
		*/
    	get("repository/:user/:repo", (req,res) ->{
    		String rawJson = recuperaRepo(req.params(":user"), req.params(":repo"));
    		Object obj = new JSONParser().parse(rawJson);
    		JSONObject jo = (JSONObject) obj;
    		return pageRepo(jo);
    		});
    }
    
    /**
     * 
     * É salva a chave da api
 
     * 
     * 
     * 
     * 
     */
    private static String recuperaRepo(String user, String repo) throws IOException {
		// TODO Auto-generated method stub
    	
    	// É salva a chave da api
    	String key = "5d76e6ca04d21839f47511dd6af6c8bcc2acd46f";
    	
    	// Criada a url para requisição na api do git
    	URL url = new URL("https://api.github.com/repos/"+ user + "/" + repo);
    	
    	// É aberta a conexão
    	HttpURLConnection con = (HttpURLConnection) url.openConnection();
    	
    	// Então são setadas as propriedades do metodo para GET, e logo após estabelecer o header para autorização com o token de acesso
    	con.setRequestMethod("GET");
    	con.setRequestProperty("Authorization","Bearer " + key);
    	
    	// É feito o request
    	con.connect();
    	//Então é feita a verificação do status de resposta. caso esteja entre 200 e 299, então foi um sucesso. Caso não, a conexão é encerrada
    	if(con.getResponseCode() < 300 && con.getResponseCode() >=200) {
    	// então é feito um processo para ler  a response e criar uma variavel String com o json puro
   		 	BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
	    	 
   		 	BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream()));
            StringBuilder sb = new StringBuilder();
            String line;
            while ((line = br.readLine()) != null) {
                sb.append(line+"\n");
            }
            
            con.disconnect();
            System.out.println(sb.toString());
            return sb.toString();	
   	 } else {
   		 con.disconnect();
   		 throw new ConnectException();
   	 }
	}

	//metodo para interagir com a api do github para recuperar um usuário
    private static String recuperaUser(String user) throws IOException {
    	// É salva a chave da api
    	String key = "5d76e6ca04d21839f47511dd6af6c8bcc2acd46f";
		 
    	// Criada a url para requisição na api do git
		 URL url = new URL("https://api.github.com/users/" + user);
		 
		// É aberta a conexão
	   	 HttpURLConnection con = (HttpURLConnection) url.openConnection();
	   	 
	   	 // Então são setadas as propriedades do metodo para GET, e logo após estabelecer o header para autorização com o token de acesso
	   	 con.setRequestMethod("GET");
	   	 con.setRequestProperty("Authorization","Bearer " + key);
	   	 
	   	 // É feito o request
	   	 con.connect();
	   	 	//Então é feita a verificação do status de resposta. caso esteja entre 200 e 299, então foi um sucesso. Caso não, a conexão é encerrada
	     if(con.getResponseCode() < 300) {
	    	 	// Então é feito um processo para ler a response e criar uma variavel String com o json puro
	    		 BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
		    	 
		    	 BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream()));
	             StringBuilder sb = new StringBuilder();
	             String line;
	             while ((line = br.readLine()) != null) {
	                 sb.append(line+"\n");
	             }
	             con.disconnect();
	             System.out.println(sb.toString());
	             return sb.toString();	
	      } else {
	    		 con.disconnect();
	    		 return null;
	    	 }

    }
    
    //Somente um metodo simples para estruturar de maneira simples para demonstrar no browser
    private static String pageRepo(JSONObject info) {
    	String estrutura = "";
    	estrutura += ("<p> Id do repositorio: " + info.get("id") + "</p>");
    	estrutura += ("<p> Nome do repositorio: " + info.get("name") + "</p>");
    	estrutura += ("<p> Criado em: " + info.get("created_at") + "</p>");
    	estrutura += ("<p> Link para clonagem: " + info.get("clone_url") + "</p>");
    	return estrutura;
    }
  //Somente um metodo simples para estruturar de maneira simples para demonstrar no browser
    private static String pageUser(JSONObject info) {
    	String estrutura = "";
    	estrutura += ("<p> Nome do usuário: " + info.get("name") + "</p>");
    	estrutura += ("<p>Nick do git: " + info.get("login") + "</p>");
    	estrutura += ("<p> link do github: " + info.get("url") +"</p>");
    	estrutura += ("<p>bio: " + info.get("bio") + "</p>");
    	return estrutura;
    }
}
