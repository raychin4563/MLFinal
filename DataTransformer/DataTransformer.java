import java.io.*;
import java.util.Map;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Arrays;
public class DataTransformer{
	ArrayList<Data> datas;
	BufferedReader bf;
	String fileName;
	public static void main(String[] args){
		if(args.length != 2){
			System.out.println("argument: inputfile outputfile");
			return;
		}
		DataTransformer df = new DataTransformer(args[0]);
		df.parse();
		df.toFile(1,args[1]);
	}
	public DataTransformer(String _fileName){
		fileName = _fileName;
		try{
			bf = new BufferedReader(new FileReader(fileName));
		}catch(Exception e){
			e.printStackTrace();
		}
		datas = new ArrayList<Data>(0);
	}
	public void parse(){
		String tmp = null;
		String[] elements;
		while(true){
			try{
				if((tmp = bf.readLine()) == null)
					break;
			}catch(Exception e){
				e.printStackTrace();
			}
			Data tmpData = new Data();
			
			elements = tmp.split(" ");
			tmpData.setType(Integer.parseInt(elements[0]));
			for(int i = 1;i < elements.length;i++){
				String[] detial = elements[i].split(":");
				tmpData.addFeature(Integer.parseInt(detial[0]),Double.parseDouble(detial[1]));
			}
			datas.add(tmpData);
		}
	}
	public void toFile(int type,String outputFileName){
		try{
			PrintStream output = new PrintStream(new File(outputFileName));
			for(Data tmpData:datas){
				tmpData.showFeatures(output,type);
			}
		}catch(Exception e){
			e.printStackTrace();
		}
		return;
	}
}
class Data{
	private int type;
	private Map<Integer,Double> features;
	public Data(){
		features = new HashMap<Integer,Double>(0);
	}
	public void setType(int _type){
		type = _type;
	}
	public int getType(){
		return type;
	}
	public void addFeature(int index,double value){
		features.put(index,value);
	}
	public void showFeatures(PrintStream out,int methodNum){
		if(methodNum == 1){
			out.printf("%d",type);
			Integer[] keys;
			keys = (features.keySet()).toArray(new Integer[0]);
			Arrays.sort(keys);
			for(int key : keys){
				if(features.get(key) > 0.01)
					out.printf(" %d:1",key);
			}
		}
		else if(methodNum == 2){
			out.printf("%d",type);
			Integer[] keys;
			keys = (features.keySet()).toArray(new Integer[0]);
			Arrays.sort(keys);
			for(int key : keys){
				out.printf(" "+key);
			}
		}
		else if(methodNum == 3){
			out.printf("%d",type);
			Integer[] keys;
			keys = (features.keySet()).toArray(new Integer[0]);
			Arrays.sort(keys);
			for(int key : keys){
				out.printf(" "+key);
			}
		}
		out.println();
	}
}
