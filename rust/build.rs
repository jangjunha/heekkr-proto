use std::io::Result;

use glob::glob;

fn main() -> Result<()> {
    let paths = glob("protos/**/*.proto")
        .unwrap()
        .map(|f| f.unwrap())
        .collect::<Vec<_>>();

    tonic_build::configure()
        .out_dir("src/")
        .include_file("lib.rs")
        .compile_well_known_types(true)
        .compile(&paths, &["protos/"])?;
    Ok(())
}
