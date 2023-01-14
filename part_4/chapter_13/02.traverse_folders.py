import os

color_list:dict[str:tuple] = {
    'red' : (255,0,0),
    'green' : (0,255,0),
    'blue' : (0,0,255),
    'white' : (255,255,255),
    'orange' : (255,165,0),
    'coral' : (255,127,80),
    'black' : (0,0,0)
}

def make_color(text:str,fg:tuple[int]=None,bg:tuple[int]=None,style=None)->str:
    # fg mean foreground color give it like (r(int),g(int),b(int))
    # bg mean background color give it like (r(int),g(int),b(int))
    # style gibe by tuple with ascci style code
    # create ASCII color string
    color_str = "\033[";

    # set foreground or text color
    if fg == None:
        color_str += "39;";
    else:
        color_str += "38;2;"
        fg_color = ";".join([str(color_code) for color_code in fg]);
        color_str += fg_color;

    # set background color
    if bg != None:
        # need to another parameter
        color_str += ";48;2;";
        fg_color = ";".join([str(color_code) for color_code in bg]);
        color_str+= fg_color;

    # add style
    if style != None :  
        style_str = ';'.join([str(style_code) for style_code in style]);
        color_str += ";" + style_str;

    color_str += "m" + text + "\033[0m";
    return color_str;


# print files
def print_files(files:tuple[str],indention:str=''):
    for file in files:
        file_name = indention+file;
        color_text = make_color(file_name,color_list['orange'],style=(3,));
        print(color_text);

# print folder
def print_folder_name(folder_name:str,indention:str=''):
    style_arrow = make_color(" > ",color_list['white'],color_list['red'],(1,6));
    dir_name = make_color(" "+folder_name,color_list['black'],color_list['orange'],(1,));
    print(indention+dir_name+style_arrow);

    
class Folder:
    def __init__(self,name:str,path:str,files:tuple=(),folders:tuple=()):
        self.name = name;
        self.path = path;
        self.files = tuple(files);
        self.folders = tuple(folders)

    # present the folder details
    def __repr__(self) -> str:
        # extract from self
        name,path,files,folders = self.name, self.path,self.files,self.folders;

        # create output str
        file_with_path = f"dir {name} -> {path}";
        files_names = f"> files({len(files)}) -> {files}"
        folder_names = f"> folders({len(folders)}) -> {[folder.name for folder in folders]}";
        
        return f"{file_with_path}\n{files_names}\n{folder_names}";

    # get files
    def get_files(self):
        return self.files;

    # get folder
    def get_folders(self):
        return self.folders;

    def show_tree(self):
        # first show the files
        # like below
        '''
        Project > 
            index.html
            READEME.md
            test > 
                libtest.js
                mathtest.js
            style >
                main.css
                index.css
        '''

        # create necessary variable
        folders:list[Folder] = [self]; # stack
        current_folders_number = len(folders);
        folder_indent = ''; # indention for folder
        file_indent = '  '; # indention for file

        while len(folders):
            # get folders and file 
            folder = folders.pop(0); # get one folder
            files = folder.get_files(); # get all file in folder
            folders_list = folder.get_folders(); # get all folders in folder
            current_folders_number -= 1; # dcrease the current folder

            # first print folder name
            print_folder_name(folder.name,folder_indent);

            # print files
            print_files(files,file_indent);

            # if folders_list exist then update the folder
            if folders_list:
                # update folders
                folders = folders + list(folders_list);

            if current_folders_number <= 0:
                current_folders_number = len(folders);
                folder_indent += "  ";
                file_indent += "  ";


if __name__ == "__main__":
    # make two folder
    test_folder = Folder('test','./project/',('libtest.js','mathtest.js'))
    style_folder = Folder('style','./project/',('main.css','index.css'));

    files = ('index.html','README.md');
    folders = (test_folder,style_folder);

    project_folder = Folder('project','./',files,folders);

    project_folder.show_tree();
